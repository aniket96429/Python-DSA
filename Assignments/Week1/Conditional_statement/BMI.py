"""
Program to calculate BMI of a person and classify it based on BMI

"""

weight = float(input("Enter the weight of the person in kgs: "))
height = float(input("Enter the height of the person in metres: "))

bmi = weight / height**2

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25.0:
    print("Normal weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 30:
    print("Obesity")
else:
    pass
