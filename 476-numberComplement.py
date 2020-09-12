def getBinaryComp(num):
    binary = ""
    finalVal = 0
    i = 0
    while num != 0:
        val = num % 2
        if(val == 0):
            finalVal += 2**i
        num = num // 2
        i += 1
    return finalVal



print(getBinaryComp(5))