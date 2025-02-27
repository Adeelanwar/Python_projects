def partitions(n, memo = {}):
    ts = 0
    if n > 1:
        for i in range(1,n):
            if memo[i] != None:
                memo[i] = partitions(n - i)
            ts += memo[i]
        return ts
    else:
        return 1
print(partitions(10))
