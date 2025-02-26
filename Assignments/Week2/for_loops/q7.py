"""
Program to repeatedly do the sum of digits of the numbers until single digit is obtained.

"""

n = int(input("Enter a number: "))


while n >= 10:
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    n = sum
print(n)

"""
OR
n = int(input("Enter a number: "))

while n >= 10:
    n = n % 10 + n // 10
 
print(n)
"""
