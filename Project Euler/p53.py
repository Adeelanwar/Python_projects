def fact(n,memory): #n >= 0
    if memory.get(n) == None:
        memory[n] = n * fact(n - 1,memory)
    return memory[n]
memo = {0: 1,1: 1}
fact(100,memo)
def ncr(n, r):
    nf = memo[n]
    rf = memo[r]
    nrf = memo[n - r]
    return int(nf / (rf * nrf))
print(ncr(23,10))
def pos(n):
    count = 0
    for i in range(1, n + 1):
        for j in range(1,i):
            if ncr(i,j) >= 10**6:
                count += 1
    return count
print(pos(100))
            
