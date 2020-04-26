Balance = 999 
Pin = 1234

def Check():
    Check = int(input("Welcome to CodingBook ATM Please Enter your pin : ")) #Checks for the pin
    if Check == Pin:
        options()
    else:
        print(" Invalid Pin Please try again ") #Dosent ask for another try.
        exit()
def options():
    print(" Choose an option ") #Ask's for options to the user
    print("--------------------------------------------------------------------------")
    option = int(input("1 : Check Balance\n2 : Deposite Funds\n3 : Withdrawl Funds\n4 : Change Pin\n"))
    print("--------------------------------------------------------------------------")
    if option == 1:
        Check_Balance()
    if option == 2:
        Deposite_funds()
    if option == 3:
        Withdrawl_Funds()
    if option == 4:
        Change_pin()
def Check_Balance():
    print("--------------------------------------------------------------------------") 
    global Balance #Global variable
    print("Your Total Balance is : $",Balance) #prints balance
    print("--------------------------------------------------------------------------")
    decide = input("If  want to go back to Mainmenu Press : Y \nIf you want to Exit Press :N\n") #Ask after every transaction whther to quit or not
    print("--------------------------------------------------------------------------")
    if (decide == 'y' or decide == 'Y'):
        options()
    elif (decide == 'n' or decide == 'N'):
        exit(" Thanks Please visit us again ")
        print("--------------------------------------------------------------------------")
def Withdrawl_Funds():
    print("--------------------------------------------------------------------------")
    withdrawl = int(input("How much Amout you want to Withdrawl : ")) #Ask's user amount to be withdrawl
    print("--------------------------------------------------------------------------")
    global Balance #Global variable 
    if withdrawl > Balance: #If the Withdrawl amount is greater than current Balance
        print("You Dont have Sufficient Funds to Withdrawl \nYour Balance is :",Balance)
        print("--------------------------------------------------------------------------")
    elif withdrawl <= 0: #If user Enters zero or a minus value
        print("You Either Entered Zero or a Minus value\nPlease retry")
        print("--------------------------------------------------------------------------")
    elif withdrawl > 0:
        Balance = Balance - withdrawl #Actual withdrawl process
        print(withdrawl,"Amount Deducted","Your new Balance is:",Balance)
        print("--------------------------------------------------------------------------")

    #print("--------------------------------------------------------------------------")
    
    decide = input("If  want to go back to Mainmenu Press : Y \nIf you want to Exit Press : N\n") #Ask after every transaction whther to quit or not
    print("--------------------------------------------------------------------------")
    if (decide == 'y' or decide == 'Y'):
        options()
    elif (decide == 'n' or decide == 'N'):
        exit("Thanks Please visit us again")
        print("--------------------------------------------------------------------------")
def Deposite_funds():
    global Balance
    Deposite = int(input("Enter the amount You want to deposite :"))
    print("--------------------------------------------------------------------------")
    if Deposite < 0: #check if amount is less than zero
        print("You Either Entered a Zero value or a Minus value.\n Exited")
        exit()
    elif Deposite > 0: #Allows only if amount is greater than zero
        Balance = Balance + Deposite
        print("You Sucessfully Deposited :",Deposite,":Amount in your account your current Balance is:",Balance)
    
    decide = input("If  want to go back to Mainmenu Press : Y \nIf you want to Exit Press : N\n") #Ask after every transaction whther to quit or not
    print("--------------------------------------------------------------------------")
    if (decide == 'y' or decide == 'Y'):
        options()
    elif (decide == 'n' or decide == 'N'):
        exit("Thanks Please visit us again")
        print("--------------------------------------------------------------------------")    
def Change_pin():
    global Pin
    Check_Pin = int(input("Enter your Current Pin : ")) 
    if Check_Pin == Pin: #Checks for current Pin
        New_Pin = int(input("Enter Your New Pin : ")) #Ask's to enter New Pin
        Pin = New_Pin #Assings new Pin to current Pin
        print("Password  Changed Succesfully:")
    else: 
        print("Sorry your request cannot be performed:") #if user enter's wrong pin
    
    decide = input("If  want to go back to Mainmenu Press : Y \nIf you want to Exit Press : N\n") #Ask after every transaction whther to quit or not
    print("--------------------------------------------------------------------------")
    if (decide == 'y' or decide == 'Y'):
        options()
    elif (decide == 'n' or decide == 'N'):
        exit("Thanks Please visit us again")
        print("--------------------------------------------------------------------------")

Check()