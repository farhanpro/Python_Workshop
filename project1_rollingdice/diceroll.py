import random
def diceroll():
    number = random.randint(1,6)
    if number == 1:
            print("-----")
            print("| 0 |")
            print("|   |")
            print("-----")
    elif number == 2:
            print("-----")
            print("| 0 |")
            print("| 0 |")
            print("-----")
    elif number == 3:
            print("------")
            print("| 0 0|")
            print("| 0  |")
            print("------")

    elif number == 4:
            print("------")
            print("| 0 0|")
            print("| 0 0|")
            print("------")

    elif number == 5:
            print("--------")
            print("| 0 0 0|")
            print("| 0   0|")
            print("--------")

    elif number == 6:
            print("--------")
            print("| 0 0 0|")
            print("| 0 0 0|")
            print("--------")

decide = input("Do you want to start? (Y/N)")
if (decide == 'Y' or  decide =='y'):
    diceroll()
elif (decide == 'N'or decide == 'n'):
    exit() 
 
roller = 1
while (roller == 1): 
    continuee = input("You want to roll it again?(Y/N)")
    if (continuee == 'Y'or continuee == 'y'):
        diceroll()
    elif (continuee == 'N'or continuee == 'n'):
        roller = 2
        exit()