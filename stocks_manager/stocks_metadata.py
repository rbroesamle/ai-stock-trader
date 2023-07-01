import pandas as pd
import os

from pathlib import Path


class StocksMetadata:
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


class Company:
    def __init__(self, name: str, symbol: str, keywords):
        self.name = name
        self.symbol = symbol
        self.keywords = keywords

    def __str__(self) -> str:
        return f'Company(name="{self.name}", symbol="{self.symbol}", keywords={self.keywords})'