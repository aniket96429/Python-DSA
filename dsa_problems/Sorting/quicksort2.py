"""
Quick sort algorithm program in descending.

"""


def partition(nums, low, high):
    pivot = nums[high]
    idx = low - 1
    for j in range(low, high):
        if nums[j] <= pivot:
            idx += 1
            nums[j], nums[idx] = nums[idx], nums[j]
    idx += 1
    nums[high], nums[idx] = nums[idx], nums[high]
    return idx


def quicksort(nums, low, high):
    if low < high:
        p_idx = partition(nums, low, high)
        quicksort(nums, low, p_idx - 1)
        quicksort(nums, p_idx + 1, high)


if __name__ == "__main__":
    nums = []
    n = int(input("Size of array: "))
    for i in range(n):
        num = int(input(f"Enter the {i+1} number: "))
        nums.append(num)
    low = 0
    high = len(nums) - 1
    quicksort(nums, low, high)
    print(f"Sorted array is: {nums}")
