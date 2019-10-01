class Solution:
    def longestCommonPrefix(self, strs: str) -> str:
        listItems = list(zip(*strs))
        prefix = ""
        
        for tuples in listItems:
            if(tuples.count(tuples[0]) == len(strs)):
                prefix += tuples[0]
            else:
                return prefix

        return prefix

sol = Solution()
print(sol.longestCommonPrefix(['dog', 'flow', 'flour']))

