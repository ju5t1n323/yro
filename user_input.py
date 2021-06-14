valid = False 
while not valid:
    try:
        inpt = int(input("please enter a whole number"))
    except ValueError:
        print("not right yet")
    if 0 < inpt < 100:
        print("yey your number was fine")
        valid = True