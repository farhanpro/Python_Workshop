print("---Tip calculator---")
bill=int(input("What was the total bill?  $:"))
tip_percent = int(input("What percent of tip you wanna give? $: "))
split = int(input("Number in  which bill will be splitted : "))
percentage = 100 * tip_percent/bill
print("The total amount each one has to pay will be : ",((bill + percentage)/split))