"""
Program to print sum of all the factors of a number.
Note - It is optimal solution with O(sqrt(N)) time complexity

"""

num = int(input("Enter the number: "))

sum = 0
for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        sum += i
        if num // i != i:
            sum += num // i

print(f"Sum is {sum}")
