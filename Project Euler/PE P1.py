def div3(n):
    lis = []
    i = 3
    while i <= n:
        lis.append(i)
        i += 3
    return set(lis)
def div5(n):
    lis = []
    i = 5
    while i <= n:
        lis.append(i)
        i += 5
    return set(lis)

def div3or5(n):
    lis = []
    i = 3
    while i <= n:
        lis.append(i)
        i += 3
    j = 5
    while j <= n:
        if j % 3 != 0:
            lis.append(j)
        j += 5
    return lis
def sumoflist(lis):
    tsum = 0
    for i in lis:
        tsum += i
    return tsum
lis = div3or5(10)
print(lis)
print(sumoflist(lis))
