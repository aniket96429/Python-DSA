"""
Program to print the multiplication table of a number given as input by user

"""

num = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(f"{num} X {i} = {num*i}")
    i += 1
