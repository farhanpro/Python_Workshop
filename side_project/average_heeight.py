studentHeight  = input("Input the list of the students heights : ").split()
for n in range(0,len(studentHeight)):
    studentHeight[n] = int(studentHeight[n])
print(studentHeight)

#print(len(studentHeight))

totalHeight = 0
for height in  studentHeight:
    totalHeight = height + totalHeight

print("Total height  should be " , totalHeight)
#print("Average of total height will be :", totalHeight / len(studentHeight) )

number = 0
for i in studentHeight : #How len function works
    number = number + 1

print("Average Should be" , totalHeight / number)
