"""
Program to check if a sequence is palindrome or not using while loop

"""


def palindrome(ls, start: int, end: int) -> bool:
    while start <= end:
        if ls[start] != ls[end]:
            return False
        start += 1
        end -= 1
    return True


# nums = [1, 2, 3, 2, 1]         # to check palindrome for a list
nums = "nitini"  # to check palindrome for a string
start = 0
end = len(nums) - 1
print(palindrome(nums, start, end))
