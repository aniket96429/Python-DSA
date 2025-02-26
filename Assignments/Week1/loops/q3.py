"""
Program to print the sum of numbers from start to end where start and end is given by user.

"""

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

i = start
sum = 0
while i <= end:
    sum += i
    i += 1

print(sum)
