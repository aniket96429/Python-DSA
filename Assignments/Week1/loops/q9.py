"""
Program to count the total even and odd numbers between start to end.

"""

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

count_odd = 0
count_even = 0
i = start
while i <= end:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    i += 1

print(f"Even = {count_even}\nOdd = {count_odd}")
