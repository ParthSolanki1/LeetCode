def countAndSay(n: int):
    start = "1"
    for i in range(n-1):
        temp = ""
        length = 0
        begins = 0
        for j in range(len(start)):
            if(start[j] == start[begins]):
                length += 1
            else:
                temp += str(length)
                temp += start[begins]
                length = 1
                begins = j
        temp += str(length)
        temp += start[-1]
        start = temp
    return start

print(countAndSay(1))
print(countAndSay(2))
print(countAndSay(3))
print(countAndSay(4))
print(countAndSay(5))



