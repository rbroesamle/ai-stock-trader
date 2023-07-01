import pandas as pd
import datetime

from pathlib import Path


class StocksManager:
    def get_companies():
        meta_df = pd.read_table("stocks_data/stocks_symbols.csv", delimiter=",")

        meta_df = meta_df[["Symbol", "Security"]]

        companies = []
        for _, row in meta_df.iterrows():
            companies.append(
                Company(
                    name=row["Security"],
                    symbol=row["Symbol"],
                    keywords=[row["Security"]],
                )
            )

        companies = [
            c for c in companies if Path(f"stocks_data/stocks/{c.symbol}.csv").is_file()
        ]

        return companies

    def get_stock_value(stock_symbol: str, date):
        df = pd.read_table(f"stocks_data/stocks/{stock_symbol}.csv", delimiter=",")
        date_string = date
        try:
            date_string = date.strftime("%Y-%m-%d")
        except ValueError:
            pass
        row = df[df["Date"] == date_string]
        value = row["Close"]
        return value.values[0]


class Company:
    def __init__(self, name: str, symbol: str, keywords):
        self.name = name
        self.symbol = symbol
        self.keywords = keywords

    def __str__(self) -> str:
        return f'Company(name="{self.name}", symbol="{self.symbol}", keywords={self.keywords})'
