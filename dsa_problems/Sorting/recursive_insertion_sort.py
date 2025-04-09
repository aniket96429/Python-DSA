"""
Recursive Insertion sort algorithm program.

"""


def insertion_sort(nums, l):
    if l <= 1:
        return
    insertion_sort(nums, l - 1)
    key = nums[l - 1]
    j = l - 2
    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key
    return


if __name__ == "__main__":
    nums = []
    n = int(input("Size of array: "))
    for i in range(n):
        num = int(input(f"Enter the {i+1} number: "))
        nums.append(num)

    insertion_sort(nums, len(nums))
    print(f"Sorted array is: {nums}")
