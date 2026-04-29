def quick_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums
    
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage
if __name__ == "__main__":  
    nums = [3, 6, 8, 10, 1, 2, 1]
    sorted_nums = quick_sort(nums)
    print(sorted_nums)