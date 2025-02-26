"""
Program to print if a number is a perfct number.

"""

num = int(input("Enter the number: "))

sum = 0
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        sum += i
        if num // i != i:
            sum += num // i

if (sum - num) == num:
    print("Yes it is a perfect number")
else:
    print("No it is not a perfect number")
