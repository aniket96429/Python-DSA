"""
Program to print the pattern

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

for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        if j % 2 == 0:
            print(2, end=" ")
        else:
            print(1, end=" ")
    print()
