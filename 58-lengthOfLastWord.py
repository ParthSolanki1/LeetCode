def lengthOfLastWord(s):
    count = 0
    i = -1
    s = s.strip()
    g = -1*len(s)
    
    while i >= g:
        if(s[i] == ' ' and i != -1):
            return count
        count += 1
        i -= 1

    return count

print(lengthOfLastWord("Hello World"))
    
