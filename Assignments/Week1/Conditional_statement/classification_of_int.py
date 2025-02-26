"""
Program that accepts an integer from user and classifies it as:

1. Positive and Even
2. Positive and Odd
3. Negative and Even
4. Negative and Odd
5. Zero

"""

try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid Input")
    exit()

if num > 0:
    if num % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif num < 0:
    if num % 2 == 0:
        print("Negative and Even")
    else:
        print("Negative and Odd")
else:
    print("Zero")
