
def get_interger_input(message, error, low, high):
    while True:
            try:
                inpt = int(input(message))
                if low < inpt < high:
                    return inpt
                else:
                    print(error)
            except ValueError:
                print(error)

coffees = get_interger_input("please enter how many coffees you had todaY")
