import pandas as pd
from filter import Filter
from article import Article

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
df["date"] = pd.to_datetime(df["date"])
df.sort_values(by="date", inplace=True, ascending=False)

company_map = {}

filter = Filter()

for index, row in df.iterrows():
    article = Article(headline=row.headline, text=row.text, date=row.date)
    companies = filter.get_relevant_companies(article)
    for company in companies:
        if company_map.get(company.stock_name) is None:
            company_map[company.stock_name] = [article]
        else:
            company_map[company.stock_name].append(article)

for company_name, article_list in company_map.items():
    print(company_name)
    for article in article_list:
        print(article.headline)
