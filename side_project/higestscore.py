StudentMarks = input("Enter marks of the Students : ").split()
max = StudentMarks[0]
for i in StudentMarks:
    if i > max:
        max = i

print("Higest marks obtained to a Student is", max)
