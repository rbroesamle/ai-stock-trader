class Company:
    def __init__(self, stock_name, possible_names):
        self.stock_name = stock_name
        self.possible_names = possible_names
        self.relevant_articles = []

    def append_relevant_article(self, article):
        self.relevant_articles.append(article)

    def get_companies(self):
        pass

    def __str__(self) -> str:
        return (
            f'Company(name="{self.stock_name}", possiblr_names="{self.possible_names}")'
        )
