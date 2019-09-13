class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in (nums[i+1:]):
                index = nums[0:i] + nums[i+1:]
                return [i, index.index(needed)+1]
            elif needed in (nums[0:i]):
                return [i, nums.index(needed)]

solution = Solution()
print(solution.twoSum([2, 7, 11, 22], 9))

