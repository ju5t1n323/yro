from random import choice
prize_money = 0

valid = False
while not valid:
    try:
        money = int(input("how much would you like to put in today?"))
        if 0 < money <= 10:
            valid = True
        else:
            print("please enter a whole number between 1 and 10")
    except ValueError:
        print("please enter a whole number  between 1 and 10")
tokens = []
horse_num = 500
zebra_num = 350
donkey_num = 100
unicorn_num = 1

for i in range(horse_num):
    tokens.append('horse')

for i in range(zebra_num):
    tokens.append('zebra')

for i in range(donkey_num):
    tokens.append('donkey')

for i in range(unicorn_num):
    tokens.append('unicorn')

    money -= 1
    token = choice(tokens)
    rewards = {'horse': 0.5, 
            'zebra': 0.5, 
            'donkey': 0, 
            'unicorn': 5}

    reward = rewards[token]

    if token == 'horse' or 'zebra':
        print(f"congradulation you got a {token} \n you win a {reward} as a prize")

    if token == "donkey":
        print(f"oh no you got {token} \n you win {reward} as a prize")

    if token == "unicorn":
        print(f"fuck yeee!!!! you got {token} \n you win {reward} as a prize")
    prize_money += reward
    print(f"your current winning {prize_money}. money left: ${money}")
    replay = input("press enter to play again \n type exit to cash out\n")
    if replay == "exit" or money <0:
        break

    print("fuck off now come back later")