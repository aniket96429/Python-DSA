"""
Program to print the pattern

* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

"""

n = int(input("Enter the number: "))

if n == 0:
    exit("0")

for i in range(n, 0, -1):
    for j in range(n, i, -1):
        print(" ", end=" ")

    for k in range(1, 2 * i):
        print("*", end=" ")

    print()
