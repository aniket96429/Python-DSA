"""
Program to print the pattern

1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15

"""

n = int(input("Enter the number: "))

if n == 0:
    print(0)
    exit()

sum = 0
for i in range(1, n + 1):
    for j in range(1, i + 1):
        sum += 1
        print(sum, end=" ")
    print()
