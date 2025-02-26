"""
Program to print the pattern

1
2 1 
3 2 1
4 3 2 1
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

"""

n = int(input("Enter the number: "))

if n == 0:
    print(0)
    exit()

for i in range(1, n // 2 + 2):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

for i in range(n // 2, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
