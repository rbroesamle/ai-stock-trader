class ChatGPT:
    def get_score(self, headline, company, mock=True):
        if mock:
            return self.get_score_randomly(headline, company)
        else:
            return self.get_score_with_chatgpt(headline, company)

    @classmethod
    def get_score_with_chatgpt(cls, headline, company):
        # TODO Lucas
        return 1

    @classmethod
    def get_score_randomly(cls, headline, company):
        # TODO Pia
        return 1
