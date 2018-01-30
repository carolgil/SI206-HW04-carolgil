import random
response = input("What is your question?")
while response != "quit" :

    if not response.endswith("?"):
        print("I'm sorry, I can only answer questions")
    else:
        possible_answers = ['Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful', "It is certain", "It is decidedly", "Without a doubt", "Yes definitiely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes",
        "Signs point to yes"]
        print(random.choice(possible_answers))

    response = input("What is your question?")
