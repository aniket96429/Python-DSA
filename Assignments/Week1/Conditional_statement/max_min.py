"""
Program to find the maximum and minimum between three numbers eter by user

"""

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"Max is {num1} and Min is {num3}")
    else:
        print(f"Max is {num1} and Min is {num2}")
elif num2 > num3 and num2 > num3:
    if num1 > num3:
        print(f"Max is {num2} and Min is {num3}")
    else:
        print(f"Max is {num2} and Min is {num1}")
else:
    if num1 > num2:
        print(f"Max is {num3} and Min is {num2}")
    else:
        print(f"Max is {num3} and Min is {num1}")
