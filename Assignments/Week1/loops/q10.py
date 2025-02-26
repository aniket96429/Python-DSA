"""
Program to print all the numbers from start to end where start can be smaller than end.

"""

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

if start <= end:
    i = start
    while i <= end:
        print(i, end=" ")
        i += 1
else:
    i = end
    while i <= start:
        print(i, end=" ")
        i += 1
