def average(marks = int(input("Enter the marks of the Student : "))):
    if (marks >= 90):
        print("You have been passed with A grade")
    elif (marks >= 65 and marks <= 89):
        print("You have been passed With B grade")
    elif (marks >= 45 and marks <= 64):
        print("You have been passed with C grade")
    elif (marks >= 35 and marks <= 44):
        print("You have been Passed with D grade")
    else:
        print("Sorry you failed")

average()
print("hie")