class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        count = 0
        for i in range(len(s)):
            if(i != (len(s)-1) and values[s[i+1]] > values[s[i]]):
                count += values[s[i:i+2]]
            elif(i == 0 or values[s[i-1]] >= values[s[i]]):
                count += values[s[i]]

        return count

check = Solution()
print(check.romanToInt('XXVII'))
print(check.romanToInt('XXVIV'))
print(check.romanToInt('CM'))

