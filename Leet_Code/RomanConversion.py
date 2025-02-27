conversion = {'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
conversion2 = {}
chars = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
length = len(chars)
for i in range(length - 1):
    for j in range(i, length):
        if i != j:
            conversion2[chars[i] + chars[j]] = conversion[chars[j]] - conversion[chars[i]]
print(conversion2)

str1 = 'M'
str2 = 'MX'
str3 = 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDCDCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCXII'
def convert(str1):
    number = 0
    str_cpy = str1
    while len(str1) >= 1:
        if str1[0: 2] in conversion2:
            number += conversion2[str1[0: 2]]
            print(str1[0:2], number)
            str1 = str1[2:]
            print(str1)
        else:
            number += conversion[str1[0]]
            print(str1[0], number)
            str1 = str1[1:]
            print(str1)
    print("%s = %g" %(str_cpy, number))
    return number

convert(str1)
convert(str2)
convert(str3)
