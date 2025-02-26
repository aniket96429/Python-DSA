"""
Program to print the pattern

    1
   101
  10101
 1010101
101010101

"""

n = int(input("Enter the number: "))

if n == 0:
    print(0)
    exit()

for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end="")
    for k in range(1, 2 * i):
        print(k % 2, end="")
    print()
