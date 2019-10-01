def searchInsert(nums, target):
    i = 0
    j = len(nums) - 1
    while(i < j):
        if nums[i] >= target:
            return i
        elif nums[j] < target:
            return j + 1
        elif nums[j] == target:
            return j
        i += 1
        j -= 1
    return i

print(searchInsert([1, 3, 5, 6], 5))
print(searchInsert([1, 3, 5, 6], 2))
print(searchInsert([1, 3, 5, 6], 7))
print(searchInsert([1, 3, 5, 6], 0))
