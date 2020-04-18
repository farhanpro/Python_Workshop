def roll():
    import random
    number = random.randint(1,6)    
if number == 1:
            print("-----")
            print("| 0 |")
            print("|   |")
            print("-----")




decide = input("Do you want to roll again?(Y/N)")
if decide == 'Y' or decide == 'y':
    print("Working")