height=input("Enter your height in foot : ")
inch=input("Enter your height in inchs : ")
weight=input("Enter your weight in kg's : ")
meter_of_foot = float(height)/3.281
meter_of_inch = float(inch)/39.37
meter = meter_of_foot + meter_of_inch
result = float(weight)/(float(meter)*float(meter))
print("From given input's your BMI should Be : ", result)

if(result <= 18.5):
    print("You are Under Weight. ")
if(result > 18.5 and result <= 25 ):
    print("You are Normal Weight. ")
if (result > 25 and result <= 30):
    print("You are Over Weight. ")
if  (result > 30 and result <= 35):
    print("You are Obese. ")
if (result > 35):
    print("You are Clinically Obese.")