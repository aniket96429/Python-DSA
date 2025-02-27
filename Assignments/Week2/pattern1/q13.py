"""
Program to print the pattern

5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5

"""

n = int(input("Enter the number: "))

if n == 0:
    exit()

for i in range(n // 2 + 1, 0, -1):
    for j in range(n // 2 + 1, i - 1, -1):
        print(j, end="  ")
    print()

for i in range(2, n // 2 + 2):
    for j in range(n // 2 + 1, i - 1, -1):
        print(j, end="  ")
    print()
