import requests
from html import unescape

response = requests.get("https://opentdb.com/api.php?amount=5&category=23&difficulty=easy&type=boolean")

questions = response.json()["results"]
# this is a intro/rules for the quiz
print('\033[95m'"""------------welcome to the history quiz------------
    hi, my name is Justin, i made this quiz by using my python skills, i hope you enjoy! 
    Now, this is how to play my quiz you read the question and then answer either True or False. 
    (make sure your spelling is correct and use capital letter for the first letter of the answer) enjoy ^;^""")
# this is to print the questions on the screen
score = 0
for i, question in enumerate(questions):
    print(f"--------------question {i + 1}--------------")
    ans = input(unescape(question["question"]))

    ans_capital = ans.capitalize()
# this tells the users whether they got the question right or not
    if ans_capital in question["correct_answer"]:
        print("correct!!!")
        score = score + 1
    else:
        print(f"incorrect, the correct answer was ",question["correct_answer"])
        

# shows the total scores
score = int(score)
print(f"your score is {score} out of 5")
# this tells the scores for the users and saying goodbye
print("Thanks for playing!")             

#TODO 
# Let user input True true T t yes Yes y Y False false F f No no n N .lower()
# Don't let the use put in any other input
# add a way to get different questions