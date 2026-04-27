def selection_sort(nums: list[int]) -> list[int]:
    n = len(nums)

    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
        
    return nums
# Time Complexity: O(n^2)
# Space Complexity: O(1)