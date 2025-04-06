"""
Selection sort algorithm program in descending order.

"""


def selection_sort(nums):
    n = len(nums)
    for i in range(0, n - 1):
        max_index = i
        for j in range(i + 1, n):
            if nums[j] > nums[max_index]:
                max_index = j
        nums[i], nums[max_index] = nums[max_index], nums[i]
    return


if __name__ == "__main__":
    nums = []
    n = int(input("Size of array: "))
    for i in range(n):
        num = int(input(f"Enter the {i+1} number: "))
        nums.append(num)

    selection_sort(nums)
    print(f"Sorted array is: {nums}")
