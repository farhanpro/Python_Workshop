import json
def dict():
   
    data = json.load(open("original.json"))
    word = input("Enter the word you want to search : ")
    converted = word.casefold()
    print(data[converted])

dict()
i = 1
while (i==1):
    decide = input("You want to search another word?(Y/N)")
    if decide == 'Y' or decide == 'y':
        dict()
    else:
        i = 0
        exit()