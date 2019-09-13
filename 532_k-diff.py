class Solution:
    def findPairs(self, nums, k: int) -> int:
        if(len(nums) == 0 or k < 0):
            return 0
        
        nums.sort()
        used = []
        start = 0
        count = 0
        end = len(nums)

        while(end != 1):
            for i in range(start, end-1):
                mindiff = abs(nums[i] - nums[end-1])
                if(mindiff == k and not((nums[i], nums[end-1]) in used)):
                    used.append((nums[i], nums[end-1]))
                    count += 1

            end = end - 1
    
        return count

a = Solution()
print(a.findPairs(, -275))



                




        