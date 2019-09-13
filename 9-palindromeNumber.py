class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        for i in range(len(y)//2):
            if(y[i] != y[-1 - i]):
                return False
        return True

a = Solution()
x = 121
y = -121
z = 10
print(a.isPalindrome(x))
print(a.isPalindrome(y))
print(a.isPalindrome(z))

