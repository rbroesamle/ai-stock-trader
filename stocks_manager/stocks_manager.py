import pandas as pd
from company import Company
from pathlib import Path
import datetime


class StocksManager:
    def get_companies(self):
        meta_df = pd.read_table("stocks_data/stocks_symbols.csv", delimiter=",")

        meta_df = meta_df[["Symbol", "Security"]]

        companies = []
        for _, row in meta_df.iterrows():
            companies.append(
                Company(
                    stock_name=row["Symbol"],
                    possible_names=[row["Security"]],
                )
            )

        companies = [
            c
            for c in companies
            if Path(f"stocks_data/stocks/{c.stock_name.upper()}.csv").is_file()
        ]

        return companies


    def get_stock_value(self, stock_symbol: str, date):
        df = pd.read_table(f"stocks_data/stocks/{stock_symbol}.csv", delimiter=",")
        date_string = date
        try:
            date_string = date.strftime("%d-%m-%Y")
        except ValueError:
            pass
        row = df[df["Date"] == date_string]
        value = row["Close"]
        if (len(value.values)) == 0:
            next_day = date + datetime.timedelta(days=1)
            return self.get_stock_value(stock_symbol, next_day)
        return value.values[0]


    def get_next_day_percentage(self, company, date):
        this_day_value_abs = self.get_stock_value(company.stock_name, date)
        date = date + datetime.timedelta(days=1)
        next_day_value_abs = self.get_stock_value(company.stock_name, date)
        percentage_inc = (next_day_value_abs - this_day_value_abs) / this_day_value_abs
        return percentage_inc
