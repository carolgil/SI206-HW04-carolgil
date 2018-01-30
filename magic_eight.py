response = input("What is your question?")
while response != "quit" :
    response = input("What is your question?")
    if response[:-1] is not "?" :
        print("I'm sorry, I can only answer questions")
