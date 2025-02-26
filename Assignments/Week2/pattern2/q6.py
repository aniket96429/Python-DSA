"""
Program to print the pattern

12345
 1234
  123
   12
    1

"""

n = int(input("Enter the number: "))

if n == 0:
    print(0)
    exit()

for i in range(n, 0, -1):
    for j in range(n, i, -1):
        print(" ", end="")
    for k in range(1, i + 1):
        print(k, end="")
    print()
