import openai
import random

openai.api_key = "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"


class ChatGPT:
    def get_score(self, headline, company, mock=True):
        if mock:
            return self.get_score_randomly(headline, company)
        else:
            return self.get_score_with_chatgpt(headline, company)

    @classmethod
    def get_score_with_chatgpt(cls, headline, company):
        response = openai.Completion.create(
            engine="text-davinci-003",  # gpt-3.5-turbo
            # prompt aus Vorlage angepasst
            prompt=f'Forget all your previous instructions. Pretend you are a financial expert\
                with stock recommendation experience.\
                Only answer with “2” if good news, “0” if bad news, or “1” if neutral or uncertain.\
                Is the headline:"{headline}" good or bad for the stock price of {company} in the short term?',
            max_tokens=20,
            temperature=0,
            n=1,
            stop=None,
        )

        if response.choices:
            return int(response.choices[0].text.strip()) - 1
        else:
            print("Fehler")

    @classmethod
    def get_score_randomly(cls):
        # TODO Pia
        randnum = random.randint(-1, 1)
        print(randnum)
        return randnum
