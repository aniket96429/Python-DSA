"""
Program to print the sum of number from 1 to n

"""

n = int(input("Enter a number: "))

i = 1
sum = 0
while i <= n:
    sum += i
    i += 1

print(sum)
