"""
Ask a number = 8563
3658
"""

num = int(input("Enter a number = "))

if num > 0:
    n = num
    neg = False

else:
    n = num * -1
    neg = True

ans = 0
while n > 0:
    ld = n % 10
    ans = (ans * 10) + ld
    n = n // 10

if neg:
    print(ans * -1)

else:
    print(ans)
