"""
Quick sort algorithm program.

"""


def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high
    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        while nums[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j


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
