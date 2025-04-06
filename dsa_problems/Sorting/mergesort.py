"""
Mergesort sort algorithm program.

"""


def merge(left, right):
    n = len(left)
    m = len(right)
    result = []
    i = j = 0
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < n:
        result.append(left[i])
        i += 1
    while j < m:
        result.append(right[j])
        j += 1

    return result


def mergesort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    sorted_left = mergesort(nums[:mid])
    sorted_right = mergesort(nums[mid:])
    return merge(sorted_left, sorted_right)


if __name__ == "__main__":
    nums = []
    n = int(input("Size of array: "))
    for i in range(n):
        num = int(input(f"Enter the {i+1} number: "))
        nums.append(num)
    print(f"Sorted array is: {mergesort(nums)}")
