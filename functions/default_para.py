def add(x=0,y=0):  #Default parameter  is someting that if a user does not insert the second value 
    #it will not show the error
    return print(x+y)

a = int(input("Enter a value for addition : "))
b = int(input("Enter second value for addition :"))
add(a)