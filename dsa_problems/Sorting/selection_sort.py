"""
Selection sort algorithm program.

"""


def selection_sort(nums):
    n = len(nums)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

    return


if __name__ == "__main__":
    nums = []
    n = int(input("Size of array: "))
    for i in range(n):
        num = int(input(f"Enter the {i+1} number: "))
        nums.append(num)

    selection_sort(nums)
    print(f"Sorted array is: {nums}")
