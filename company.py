class Company:
    def __init__(self, real_name, possible_names):
        self.real_name = real_name
        self.possible_names = possible_names
        self.relevant_articles = []

    def append_relevant_article(self, article):
        self.relevant_articles.append(article)

    def get_companies(self):
        pass