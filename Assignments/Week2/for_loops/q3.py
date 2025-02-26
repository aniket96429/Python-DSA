"""
Program to count all the factors of a number.
Note - It is optimal solution with O(sqrt(N)) time complexity

"""

num = int(input("Enter the number: "))

count = 0
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        count += 1
        if num // i != i:
            count += 1

print(f"Total factors are: {count}")
