def fact(n, mem = {}): #n >= 0   
    if n <= 1:
        return mem[1]
    else:
        if mem.get(n) == None:
            z = n * fact(n - 1, mem)
            mem[n] = z
            print(mem)
            return z, mem
        else:
            return (mem[n], mem)
    
def s(n, mem):
    for i in range(10000):
        fac = fact(i, mem)
        mem = fac[1]
        if fac[0] % n == 0:
            break
    return i

def S(n):           
    memo = {1: 1}
    TS = 0
    for i in range(2, n + 1):
        TS += s(i, memo)
    print(TS)
    return TS
S(5)
