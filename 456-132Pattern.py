def find132pattern(nums: int) -> bool:
    if (len(nums) < 3):
        return False
        
    for i in range(len(nums)-2):
        if(nums[i] < nums[i+2] and nums[i+2] < nums[i+1]):
            return True
    
    return False

print(find132pattern([3, 1, 4, 2]))