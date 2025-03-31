"""
Program to check if a sequence is palindrome or not using recursion

"""


def palindrome(ls, start: int, end: int):
    if start > end:
        return True
    if ls[start] != ls[end]:
        return False
    return palindrome(ls, start + 1, end - 1)


# nums = [1, 2, 3, 3, 1]  # to check palindrome for a list
nums = "nitin"  # to check palindrome for a string
start = 0
end = len(nums) - 1
print(palindrome(nums, start, end))
