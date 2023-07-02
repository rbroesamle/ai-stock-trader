import numpy as np
from sklearn.linear_model import LinearRegression


def get_x_y_array_from_companies(all_companies):
    all_x_y_tuples = []
    for company in all_companies:
        for score in company.average_scores:
            all_x_y_tuples.append((score[1], score[2]))
    all_x_list = [i for i, j in all_x_y_tuples]
    all_y_list = [j for i, j in all_x_y_tuples]
    return np.array(all_x_list).reshape((-1, 1)), np.array(all_y_list)


def create_lin_regression_model(all_companies):
    model = LinearRegression(n_jobs=-1)
    x_y_vals = get_x_y_array_from_companies(all_companies)
    model.fit(*x_y_vals)
    r_sq = model.score(*x_y_vals)
    print(f"coefficient of determination: {r_sq}")
    print(f"when score is 0, the price changes by: {model.intercept_} %")
    normalized_model_slope = model.coef_ / 10
    print(
        f"when score is increased by 0.1, prediction changes by: {normalized_model_slope}"
    )
    return model, x_y_vals
