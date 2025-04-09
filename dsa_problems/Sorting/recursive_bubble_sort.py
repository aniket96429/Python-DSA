"""
Recursive Bubble sort algorithm program.

"""


def bubble_sort(nums, l):
    if l <= 1:
        return
    is_swap = False
    for i in range(l - 1):
        if nums[i + 1] < nums[i]:
            nums[i + 1], nums[i] = nums[i], nums[i + 1]
            is_swap = True

    if not is_swap:
        return
    bubble_sort(nums, l - 1)


if __name__ == "__main__":
    nums = []
    n = int(input("Size of array: "))
    for i in range(n):
        num = int(input(f"Enter the {i+1} number: "))
        nums.append(num)

    bubble_sort(nums, len(nums))
    print(f"Sorted array is: {nums}")
