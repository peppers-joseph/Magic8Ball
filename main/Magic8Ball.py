"""

"""

import random

class Magic8Ball:
    def __init__(self):
        self.responses =[
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy, try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"
        ]

    def get_response(self, index):
        return self.responses[index]

    def get_random_number(self):
        rand_number = random.randint(0,19)
        return rand_number

    def ask_a_question(self):
        user_question = input("Ask me a question:")
        if user_question[-1] != "?":
            raise ValueError("You did not ask a question!")
        #rand_num = self.get_random_number()
        #response = self.get_response(rand_num)
        #print(response)
        return(self.get_response(self.get_random_number()))

if __name__ == "__main__":
    m8 = Magic8Ball()
    print(m8.ask_a_question())
