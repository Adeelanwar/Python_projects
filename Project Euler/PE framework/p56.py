max_sum = 0
def digitsum(n):
    strn = str(n)
    tsum = 0
    for l in strn:
        tsum += int(l)
    return tsum
for a in range(1,100):
    for b in range(1,100):
        dsum = digitsum(a**b)
        if dsum > max_sum:
            print(a,b, a**b, dsum)
            max_sum = dsum
print(max_sum)
