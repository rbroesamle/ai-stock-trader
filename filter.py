

class Filter:
    def __init__(self):
        self.company_names = Rapha.get_company_names()

    def get_relevant_companies(self, article):
        relevant_companies = self.filter_company_names(article)

    def filter_company_names(self, article):
        company_names_in_article = []
        for company_real_name in self.company_names:
            for company_possible_name in self.company_names[company_real_name]:
                if company_possible_name in article.text:
                    company_names_in_article.append(company_real_name) if company_real_name not in \
                                                                          company_names_in_article else None

        return company_names_in_article

