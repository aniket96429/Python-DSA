"""
Insertion sort algorithm program in descending order.

"""


def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] < key:
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

    insertion_sort(nums)
    print(f"Sorted array is: {nums}")
