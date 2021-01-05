import random

user = int(input("Enter 1 for Rock\nEnter 2 for Paper\nEnter 3 for Scissor\nEnter your Decision : " ))
comp = random.randint(1,3)
print ("Comp's decision : ",comp)
if((user == 1 and comp == 1) or (user == 2 and comp == 2) or (user == 3 and comp == 3) or (comp == 1 and user == 1) or (comp == 2 and user == 2) or (comp == 3 and user == 3)):
    print("Draw")
if((user == 1 and comp == 2) or (user == 3 and comp == 1) or (comp == 1 and user == 3) or (user == 2 and comp == 3 )) :
    print("Comp 2 Wins")
if((user == 1 and comp == 3) or (user == 2 and comp == 1) or (comp == 1 and user == 2) or (user == 1 and comp == 3) or (user == 3 and comp == 2 )):
    print("Player 1 Wins")

