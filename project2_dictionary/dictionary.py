import json
data = json.load(open("original.json")) 

def dict():
    word = input("Enter the word you want to search : ")
    converted = word.casefold()
    if converted in data or type(converted) == list :   #Correction made  
        num = 0
        for item in data[converted]:
             num = num+1
             print(num,item)
    else:
        print("Check the word you Entered")
    
dict()
i = 1
while (i==1):
    decide = input("You want to search another word?(Y/N)")
    if decide == 'Y' or decide == 'y':
        dict()
    else:
        i = 0
        exit()