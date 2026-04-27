def bubble_sort(nums: list[int]) -> list[int]:
    n = len(nums)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums
# Time Complexity: O(n^2)
# Space Complexity: O(1)