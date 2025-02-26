"""
Program to print the pattern

1
3 2
4 5 6
10 9 8 7
11 12 13 14 15

"""

n = int(input("Enter the number: "))

if n == 0:
    print(0)
    exit()

sum = 1
for i in range(1, n + 1):
    if i % 2 != 0:
        for j in range(1, i + 1):
            print(sum, end=" ")
            sum += 1
    else:
        sum = sum + i
        for k in range(sum - 1, sum - i - 1, -1):
            print(k, end=" ")
    print()
