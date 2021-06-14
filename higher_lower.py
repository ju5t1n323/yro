import random
num = random.randint(1, 100)
while True:
    print('Guess a number between 1 and 100')
    guess = input()
    i = int(guess)
    if i == num:
        print('if you gussed less than 10 times you won')
        break 
    elif i < num:
               print('Higher')
    elif i > num:
               print('Lower')
#any recommendations for the game end                           
print('YOU WON!!!!!, would you like to play 1 more?')                                                                                                                                            