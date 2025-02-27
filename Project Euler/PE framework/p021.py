def zhi(n):
    count = 0
    for i in range(1,int(n / 2) + 1):
        if n % i == 0:
            count += i
    return count
print(zhi(284))
total_sum = 0
amiciblelist = []
for a in range(1, 10000):
    z = zhi(a)
    if not a in amiciblelist:
        if zhi(z) == a and z != a:
            amiciblelist.append(a)
            amiciblelist.append(z)
            total_sum += a + z
print(total_sum)
        
