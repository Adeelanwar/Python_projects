def zhi(n):
    count = 0
    for i in range(1,int(n / 2) + 1):
        if n % i == 0:
            count += i
    return count
abdlist = []
for a in range(1, 20162):
    if a < zhi(a):
        abdlist.append(a)

        
 
