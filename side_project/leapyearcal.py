year = int(input("Enter the Year You want to check : "))
if(year % 4 == 0):
    if(year % 100 != 0):
        print("leap")
    if(year % 400 == 0):
        print("leap")
else:
    print("Not leap")