import requests
from html import unescape

response = requests.get("https://opentdb.com/api.php?amount=15&category=23&difficulty=easy&type=boolean")

questions = response.json()["results"]

print('\033[95m'"""------------welcome to the wild no heros 's villains------------
    hi, my name is Justin ummmmmm, i made this quiz using my python skills i hope you enjoy! 
    Now, this is how to play my quiz you rread the question and then answer either True or False. 
    (make sure your spelling is correct and use capital letter for the first letter of the answer) enjoy ^;^""")
score = 0
for i, question in enumerate(questions):
    print(f"--------------question {i + 1}--------------")
    ans = input(unescape(question["question"]))

    if ans == question["correct_answer"]:
        print("correct!!!")
        score = score + 1
    else:
        print(f"incorrect, the correct answer was ",question["correct_answer"])
        


score = int(score)

print(f"your score is {score}")