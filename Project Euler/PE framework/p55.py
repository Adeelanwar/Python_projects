import string
def ispalen(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]: return ispalen(string[1:-1])
        else: return False
lycnum = []
for num in range(1,10001):
    k = str(num)
    for i in range(49):
        k = str(int(k) + int(k[::-1]))
        if ispalen(k):
            lycnum.append(num)
            break
ans = 10000 - len(lycnum)
