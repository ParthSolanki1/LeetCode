class Solution:
    def isValid(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        opposite = {'(':')', '[':']', '{':'}'}
        incorrect = ')}]'

        if(len(s)%2 != 0):
            return False

        while(s != ''):
            if '()' in s:
                index = s.find('()')
                s = s[:index] + s[index+2:]
            elif '[]' in s:
                index = s.find('[]')
                s = s[:index] + s[index+2:]
            elif '{}' in s:
                index = s.find('{}')
                s = s[:index] + s[index+2:]
            else:
                return False
        
        return True

g = Solution()
print(g.isValid("[({(())}[()])]"))