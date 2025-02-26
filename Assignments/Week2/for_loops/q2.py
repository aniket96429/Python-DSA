"""
Program to print all the factors of a number.
Note - It is optimal solution with O(sqrt(N)) time complexity

"""

num = int(input("Enter the number: "))

for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        print(i, end=" ")
        if num // i != i:
            print(num // i, end=" ")
