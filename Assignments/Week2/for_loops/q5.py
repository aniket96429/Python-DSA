"""
Program to print if a number is prime or not
Note - It is optimal solution with O(sqrt(N)) time complexity

"""

num = int(input("Enter the number: "))

if num == 1:
    print("1 is not a prime not composite")
    exit()
is_prime = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False

if is_prime:
    print("It is a prime number")
else:
    print("It is not a prime number")
