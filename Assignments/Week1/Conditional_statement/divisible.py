"""
Program to check if a number is divisible by 2, 3  and 5

"""

num = int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
    print("Yes")
else:
    print("No")
