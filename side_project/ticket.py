height = float(input("Enter your Height : "))

if(height<3):
    print("You are too small for the ride ")
else:
    print("You can enjoy the ride ")
    age = int(input("Enter your age : "))
    if ( age < 8):
        print("Your ticket  price is : 5$ ")
        photo = input("Do you want a photo graph on your ticket with extra cost 0.5 : ")
        if(photo == 'yes' or photo == 'Yes' or photo == 'YES'):
            print("For phot you have to pay extra 0.5 your total amount is $5.5")
        else:
            print("Your Final  ticket  price is : 5$ ")
    else:
        print("Your ticket price is : 8$")
        photo = input("Do you want a photo graph on your ticket with extra cost 0.5 : ")
        if(photo == 'yes' or photo == 'Yes' or photo == 'YES'):
            print("For phot you have to pay extra 0.5 your total amount is $8.5")
        else:
            print("Your Final  ticket  price is : $8 ")
