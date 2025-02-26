"""
Program to print all the numbers which is divisible by 2, 3 and 5 from start to end.

"""

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

i = start
while i <= end:
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
    i += 1
