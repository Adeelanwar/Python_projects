lfact = [0, 1]
for i in range(2,100 + 1):
    lfact.append(lfact[-1] * i)
value = 0
def ncr(n, r):
    return int(lfact[n] / (lfact[r] * lfact[n - r])) 
for n in range(1, 100 + 1):
    for r in range(1, n):
        if ncr(n, r) > 10**6:
            value += 1

print(value)
