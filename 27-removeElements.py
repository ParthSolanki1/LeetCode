def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if(nums[i] == val):
            nums[:] = nums[:i] + nums[i+1:]
        else:
            i +=1

    return len(nums)

a = [2, 3, 3, 2]
print(removeElement(a, 2))
print(a)
    