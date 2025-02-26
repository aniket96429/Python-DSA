"""
Python program to determine if a student is eligible for college admission based on criteria

maths > 70
science > 65
english > 60
total > 200
"""

math = int(input("Enter the marks of math subject : "))
science = int(input("Enter the marks of science subject : "))
english = int(input("Enter the marks of english subject : "))

if math >= 70 and science >= 65 and english >= 60 and (math + science + english) >= 200:
    print("Eligible for Admission")
else:
    print("Not eligible for Admission")
