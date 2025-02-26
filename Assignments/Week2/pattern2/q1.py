"""
Program to print the pattern

        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

"""

n = int(input("Enter the number: "))

if n == 0:
    print(0)
    exit()

for i in range(1, n + 1):
    for j in range(n, i, -1):
        print(" ", end=" ")

    for k in range(1, 2 * i):
        print("*", end=" ")

    print()
