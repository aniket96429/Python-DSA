"""
Program to repeatedly do the sum of digits of the numbers until single digit is obtained.
O(1) time complexity
"""

n = int(input("Enter the number: "))

if n > 0:
    sum = 1 + (n - 1) % 9
    print(sum)
else:
    print(0)
