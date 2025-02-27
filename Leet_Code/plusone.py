def plusOne(digits):
    i = len(digits) - 1
    while(i >= 0 and digits[i] == 9):
        digits[i] = 0
        if i == 0:
            digits.insert(0, 1)
            return digits
        i -= 1
    digits[i] = digits[i] + 1
    return digits

print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))
print(plusOne([9, 9]))