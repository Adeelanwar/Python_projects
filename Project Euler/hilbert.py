import sys
r = 27
s = 1
def func(n):
    lists = []
    for i in range(1, n + 1):
        j = 0
        while (1):
            if len(lists) == j:
                lists.append([i])
                break
            else:
                if((lists[j][-1] + i)**(1/2) % 1 == 0):
                    lists[j].append(i)
                    break
                else:
                    j += 1
    i = 0
    for lis in lists:
        i += 1
        print(i,lis)
        
def init(k):
    if k == 1:
        return 1
    if k == 2:
        return 2
    if k == 3:
        return 4
    if k >= 4:
        if k % 2 == 0:
           k = int(k / 2)
           return 2*k**2
        else:
            k = int(k / 2) + 1
            return 2*k**2 - 2*k
        
def findfr(n):
    ltups = []
    for i in range(r + 1):
        for j in range(s + 1):
            k = 2 ** i * 3 ** j
            ltups.append((int(n / k), k))
    return ltups

def evenfr(f, r):
    if f == 2:
        if r % 2 == 0:
            return oddfr(1, r + 1) + 1
        else:
           return oddfr(1, r + 1) - 1 
    else:
        n = int(f / 2) - 1
        m = int(r / 2)
        return (evenfr(2, r) + n*(4 * m + 6) + 2*(n - 1)*(n))
def oddfr(f, r):
    if f == 1:
        return int(0.5*(r**2 + r))
    if f == 3:
        if r % 2 == 0:
            return fr(2,r) - 2
        else:
            return fr(2,r) + 2
    else:
        intf = int(f)
        if r % 2 == 0:
            return fr(f - 1,r) - f + 1
        else:
            return fr(f - 1,r) + f - 1
def fr(f, r):
    if f % 2 == 0:
        return evenfr(f, r)
    else:
        return oddfr(f, r)
##    if f == 1:
##        return int(0.5*(r**2 + r))
##    if f == 2:
##        return fr(1, r + 1) + 1
##    if f == 3:
##        if r % 2 == 0:
##            return fr(2,r) - 2
##        else:
##            return fr(2,r) + 2
##    if f % 2 == 0:
##        return (fr(f - 2, r) + int(r / 2)*4 + r - 2 + r)
##    else:
##        intf = int(f)
##        if r % 2 == 0:
##            return fr(2,r) - f
##        else:
##            return fr(2,r) + f
##    if f >= 1:
##        if f % 2 == 0 or f == 1:
##            insqr = f + 1
##        else:
##            insqr = f
##        totalsqr = insqr + (r - 1)
##        print(totalsqr,totalsqr**2)
##        value = init(f)
##        while insqr <= totalsqr - 1:
##            value = insqr ** 2 - value
##            insqr += 1
##        return value
ltup = findfr((2 ** r) * (3 ** s))
sumn = 0
for tup in ltup:
    k = fr(tup[0],tup[1])
    sumn += k
print(sumn % 10**8)
