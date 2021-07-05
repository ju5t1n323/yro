import random
import os 

def get_int_input(message, error, low, high):
    while True:
        try:
            inpt = int(input(message))
            if low < inpt < high:
                return inpt
            else:
                print(error)
        except ValueError:
            print(error)

def roll_dice():
    return random.randint(1, 6)

def roll_two_dice():
    return roll_dice() + roll_dice()

cars = []
positions = []
for i in range(12):
    cars.append(0)

car_choice = get_int_input ("choose a car \n", f"please enter a number from 1 to {len(cars)}", 0, len(cars) + 1)

race_distance = get_int_input("choose a race distance\n", "please enter a number between 5 and 15", 4,31)
os.system("cls")
while len([i for i in cars if i >= 15]) < 3:
    for i, car in enumerate(cars):
        if car >= race_distance:
            print("\033[1;31;40m " + '_'*car + 'o^o>')
        elif i == car_choice -1:
            print("\033[1;32;40m " + '_'*car + 'o^o>')
        else:
            print("\033[1;33;40m " + '_'*car + 'o^o>')

    input("push enter to continue")
    os.system('cls')
    roll = roll_two_dice()-1
    if cars[roll] < 15:
        cars[roll] += 1
        if cars[roll] == 15:
            positions.append(roll + 1)

winning_car = positions[0]

print(f"car {winning_car} won!")
if winning_car == car_choice:
    print("well done, Happy?")
else:
    print("you didn't pick the winner \n better luck next time")

for i, car in enumerate(positions):
    print(f"car number {car} came in position {i +1}")

