"""
Program to print the pattern

5
4 5 
3 4 5
2 3 4 5
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5

"""

n = int(input("Enter the number: "))

if n == 0:
    print(0)
    exit()

for i in range(n // 2 + 1, 0, -1):
    for j in range(i, n // 2 + 2):
        print(j, end=" ")
    print()

for i in range(2, n // 2 + 2):
    for j in range(i, n // 2 + 2):
        print(j, end=" ")
    print()
