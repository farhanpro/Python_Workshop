import random
number = int(input("Enter what should be the length of your password : "))
i = 0
temp = ' '
letter =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!','@','#','$','%','&','*']
numbers = ['0','1','2','3','4','5','6','7','8','9']

while(i<number):
        pass1 = random.choice(letter)
        pass2 = random.choice(symbols)
        pass3 = random.choice(numbers)
        endpass = pass1 + pass2 + pass3
        temp =  endpass + temp
        i = i+3

print("Your random password is : ",temp)
