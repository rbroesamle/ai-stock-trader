import pandas as pd
import statistics
from filter import Filter
from article import Article
from chatgpt import ChatGPT
from company import Company
import numpy as np
from sklearn.linear_model import LinearRegression
import lin_regression
import datetime
from stocks_manager.stocks_manager import StocksManager
import matplotlib.pyplot as plt
import json
import threading
import supervisor

FROM_FILE_PATH = ""  # creates new model from datasets if empty
DATE_START = datetime.date(2000, 5, 19)
DATE_END = datetime.date(2000, 5, 17)

stock_supervisor = threading.Thread(
    target=supervisor.supervise_bought_stocks, args=[], daemon=True
)
stock_supervisor.start()

# news_supervisor = threading.Thread(target=supervisor.supervise_news, args=[], daemon=True)
# news_supervisor.start()

if len(FROM_FILE_PATH) == 0:
    df = pd.read_csv("data/news_articles.csv")
    df = df[["Date published", "Category", "Headline", "Article text"]]
    df = df.rename(
        columns={
            "Date published": "date",
            "Category": "category",
            "Headline": "headline",
            "Article text": "text",
        }
    )
    df["date"] = pd.to_datetime(df["date"]).dt.date
    rslt_df = df.loc[(DATE_START <= df["date"]) & (DATE_END <= df["date"])]
    print(len(rslt_df))
    rslt_df.sort_values(by="date", inplace=True, ascending=False)

    company_map = {}

    filter = Filter()

    for index, row in rslt_df.iterrows():
        article = Article(headline=row.headline, text=row.text, date=row.date)
        companies = filter.get_relevant_companies(article)
        for company in companies:
            if company_map.get(company.stock_name) is None:
                company_map[company.stock_name] = [article]
            else:
                company_map[company.stock_name].append(article)

    company_score_map = {}

    for company, article_list in company_map.items():
        for article in article_list:
            score = ChatGPT().get_score(article.headline, company, mock=True)
            if company_score_map.get(company) is None:
                company_score_map[company] = [(article.date, score)]
            else:
                company_score_map[company].append((article.date, score))

    companies_with_scores = []

    for company_name, score_list in company_score_map.items():
        scores_of_following_dates = []
        company = Company(company_name, [])
        for index, score in enumerate(score_list):
            scores_of_following_dates.append(score[1])
            if index == len(score_list) - 1 or score[0] != score_list[index + 1][0]:
                scores_of_following_dates.append(score[1])
                average_score = statistics.mean(scores_of_following_dates)
                stock_return_percentage = StocksManager().get_next_day_percentage(
                    company, score[0]
                )
                company.average_scores.append(
                    (score[0], average_score, stock_return_percentage)
                )
                scores_of_following_dates = []
        companies_with_scores.append(company)
    lin_regression_model, x_y_vals = lin_regression.create_lin_regression_model(
        companies_with_scores
    )
else:
    (
        lin_regression_model,
        x_y_vals,
    ) = lin_regression.create_lin_regression_model_from_file(FROM_FILE_PATH)

dictionary = {"x": x_y_vals[0].tolist(), "y": x_y_vals[1].tolist()}
json_object = json.dumps(dictionary, indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

plt.scatter(x_y_vals[0].reshape((-1, 1)), x_y_vals[1], color="black")
plt.plot(
    x_y_vals[0].reshape((-1, 1)),
    lin_regression_model.predict(x_y_vals[0].reshape((-1, 1))),
    color="blue",
    linewidth=3,
)
plt.xticks(())
plt.yticks(())

plt.show()
