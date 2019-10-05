def plusOne(digits):
    i = -1
    maxIndex = -1*len(digits)
    while(i >= maxIndex and digits[i] == 9):
        digits[i] = 0
        i -= 1
    if(i < maxIndex):
        return [1] + [0]*len(digits)
    digits[i] = digits[i] + 1
    return digits

print(plusOne([1, 2, 4]))
print(plusOne([1, 2, 9]))
print(plusOne([9, 9, 9]))

