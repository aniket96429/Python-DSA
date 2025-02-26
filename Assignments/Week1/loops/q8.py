"""
Program to print all the numbers which is divisible by n from start to end.

"""

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
num = int(input("Enter the number: "))

i = start
while i <= end:
    if i % num == 0:
        print(i, end=" ")
    i += 1
