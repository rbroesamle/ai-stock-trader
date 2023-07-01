import pandas as pd


class StocksMetadata:
    def get_companies():
        meta_df = pd.read_table("stocks_data/symbols_valid_meta.csv", delimiter=",")

        meta_df = meta_df[["Symbol", "Security Name"]]

        companies = []
        for _, row in meta_df.iterrows():
            companies.append(
                Company(
                    name=row["Security Name"],
                    symbol=row["Symbol"],
                    keywords=row["Security Name"],
                )
            )

        return meta_df


class Company:
    def __init__(self, name: str, symbol: str, keywords):
        self.name = name
        self.symbol = symbol
        self.keywords = keywords
