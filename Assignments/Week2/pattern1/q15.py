"""
Program to print the pattern

5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5

"""

n = int(input("Enter the number: "))

if n == 0:
    print(0)
    exit()

for i in range(n // 2 + 1, 0, -1):
    for j in range(n // 2 + 1, i - 1, -1):
        print(i, end=" ")
    print()

for i in range(2, n // 2 + 2):
    for j in range(n // 2 + 1, i - 1, -1):
        print(i, end=" ")
    print()
