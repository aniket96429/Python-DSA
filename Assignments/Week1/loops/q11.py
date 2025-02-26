"""
Program to print the pattern

n = 2 -> 1 2
n = 5 -> 1 2 4 8 16

"""

n = int(input("Enter the number: "))

i = 1
ans = 1
while i <= n:
    print(ans, end=" ")
    ans *= 2
    i += 1
