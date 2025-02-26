"""
Program to print the pattern

n = 2 -> 1 11
n = 5 -> 1 11 111 1111 11111

"""

n = int(input("Enter the number: "))

i = 1
while i <= n:
    print("1" * i, end=" ")
    i += 1
