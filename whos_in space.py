import requests

response = requests.get("https://opentdb.com/api.php?amount=10&category=21&difficulty=hard&type=multiple")

questions = response.json()["results"]
print(response.json())

for i, question in enumerate(questions):
    print(f"----------Question {i}--------------")
    print(question["question"])
    print(question["correct_answer"])
    for wrong_ans in question["incorrect_answers"]:
        print(wrong_ans)