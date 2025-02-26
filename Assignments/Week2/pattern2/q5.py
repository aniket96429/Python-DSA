"""
Program to print the pattern

*****
*   *
*   *
*   *
*****

"""

n = int(input("Enter the number: "))

if n == 0:
    print(0)
    exit()

for i in range(1, n + 1):
    if i == 1 or i == n:
        print(n * "*", end="")
    else:
        print("*" + (n - 2) * " " + "*", end="")
    print()
