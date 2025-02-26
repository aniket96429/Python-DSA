"""
Program to print the pattern

1
1 2
1 2 1
1 2 1 2
1 2 1 2 1
1 2 1 2
1 2 1
1 2
1

"""

n = int(input("Enter the number: "))

if n == 0:
    print(0)
    exit()

for i in range(1, n // 2 + 2):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print(2, end=" ")
        else:
            print(1, end=" ")
    print()

for i in range(n // 2, 0, -1):
    for j in range(1, i + 1):
        if j % 2 == 0:
            print(2, end=" ")
        else:
            print(1, end=" ")
    print()
