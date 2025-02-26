"""
Program to print the number from n ot -n

"""

n = int(input("Enter a number: "))

i = n
while i >= -n:
    print(i, end=" ")
    i -= 1
