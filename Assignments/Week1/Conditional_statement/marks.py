"""
Python program to calculate the grade of the student based on three subject marks

>90 - A
> 80 and <= 90 - B
> 70 and <= 80 - C
> 60 and <= 70 - D
<= 60 Fail
"""

marks1 = int(input("Enter the marks of subject one : "))
marks2 = int(input("Enter the marks of subject two : "))
marks3 = int(input("Enter the marks of subject three : "))

avg = (marks1 + marks2 + marks3) / 3
if avg > 90:
    print("Grade A")
elif avg <= 90 and avg > 80:
    print("Grade B")
elif avg <= 80 and avg > 70:
    print("Grade C")
elif avg <= 70 and avg > 60:
    print("Grade D")
else:
    print("Fail")
