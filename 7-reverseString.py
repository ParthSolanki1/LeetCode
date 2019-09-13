class Solution:
    def reverse(self, x: int) -> int:

        y = str(x)
        z = ''

        for i in range(len(y)):
            z += y[-1 - i]

        if x < 0 and int('-'+z[:-1]) >= -2147483648:
            return int('-'+z[:-1])
        elif x>0 and int(z) <= 2147483647:
            return int(z)
        return 0

s = Solution()
print(s.reverse(-123))
        
