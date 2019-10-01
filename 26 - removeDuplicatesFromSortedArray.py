class Solution:
    def removeDuplicates(self, nums):
        i = 1
        last = 1
        while i < len(nums):
            if nums[i] not in (nums[:i]):
                nums[last] = nums[i]
                last +=1
            i+=1
        nums[:] = nums[:last]
        return len(nums)

a = Solution()
b = [1, 1, 2]
print(a.removeDuplicates(b))
print(b)