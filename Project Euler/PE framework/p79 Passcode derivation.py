file = open('p079_keylog.txt','r')
digits = [0] * 10
for num in file:
    for i in str(int(num)):
        x = int(i)
        digits[x] = 1
print(digits)
