"""
Program to print the pattern

5
4 5 
3 4 5
2 3 4 5
1 2 3 4 5

"""

n = int(input("Enter the number: "))

if n == 0:
    print(0)
    exit()

for i in range(n, 0, -1):
    for j in range(i, n + 1):
        print(j, end=" ")
    print()
