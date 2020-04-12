age = int(input("Enter you age to place your Vote : "))
if age >= 18 and age > 0:
    print("You are Eligible to place your vote.  ")
elif age <= 18  and age > 0 :
    print("You are Not Eligible to place your vote.  ")
else:
    print("Negative number inserted")