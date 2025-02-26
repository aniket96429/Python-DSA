"""
Program to calculate the factorial of a number

"""

num = int(input("Enter the nummber: "))

fact = 1
for i in range(num, 0, -1):
    fact *= i

print(fact)
