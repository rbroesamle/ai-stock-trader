import company as cmp
from strsimpy.optimal_string_alignment import OptimalStringAlignment


def add_article_to_companies(companies, article):
    for company in companies:
        company.append_relevant_article(article)


def calculate_normalized_osa(string1, string2):
    optimal_string_alignment = OptimalStringAlignment()
    dist = optimal_string_alignment.distance(string1, string2)
    normalized_similarity = 1 - (2*dist)/(len(string1)+len(string2)+dist)
    return normalized_similarity


def delete_duplicate_articles(this_company):
    no_duplicate_articles = []
    append = True
    for i in range(0, len(this_company.relevant_articles)):
        for j in range(i+1, len(this_company.relevant_articles)):
            if calculate_normalized_osa(this_company.relevant_articles[i].headline,
                                        this_company.relevant_articles[j].headline) > 0.6:
                append = False
                break
        no_duplicate_articles.append(this_company.relevant_articles[i]) if append else None
        append = True
    this_company.relevant_articles = no_duplicate_articles


class Filter:
    def __init__(self):
        self.companies = Rapha.get_companies()

    def get_companies_with_articles(self, articles):
        for this_article in articles:
            this_relevant_companies = self.get_relevant_companies(this_article)
            add_article_to_companies(this_relevant_companies, this_article)
        for this_company in self.companies:
            delete_duplicate_articles(this_company)

    def get_relevant_companies(self, article):
        relevant_companies = self.filter_company_names(article)
        return relevant_companies

    def filter_company_names(self, article):
        company_names_in_article = []
        for this_company in self.companies:
            for company_possible_name in this_company.possible_names:
                if company_possible_name in article.text:
                    company_names_in_article.append(this_company) if this_company not in company_names_in_article \
                        else None
        return company_names_in_article



