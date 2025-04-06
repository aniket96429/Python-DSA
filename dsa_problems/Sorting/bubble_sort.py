"""
Bubble sort algorithm program.

"""


def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 2, -1, -1):
        is_swap = False
        for j in range(0, i + 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_swap = True

        if is_swap == False:
            break
    return


if __name__ == "__main__":
    nums = []
    n = int(input("Size of array: "))
    for i in range(n):
        num = int(input(f"Enter the {i+1} number: "))
        nums.append(num)

    bubble_sort(nums)
    print(f"Sorted array is: {nums}")
