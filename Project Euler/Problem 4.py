def ispal(n):
    i = str(n)
    if len(i) <= 1:
        return True
    if i[0] == i[-1]:
        return ispal(i[1:-1])
    else:
        return False
result = 0
for i in range(101,1000):
    for j in range(101,1000):
        n = i * j
        if (ispal(n)):
            print(i, j, n)
            if result <= n:
                result = n
    
    
