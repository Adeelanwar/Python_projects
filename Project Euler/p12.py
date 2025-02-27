def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]
def fact(n):
    if n > 1:
        return n * fact(n - 1)
    else:
        return 1
listofprimes = primes_sieve1(1000000)
def pdiv(n):
    i = 0
    divs = {}
    while n > 1:
        p = listofprimes[i]
        while n % p == 0:
            if divs.get(p) ==  None:
                divs[p] = 1
            else:
                divs[p] += 1
            n = int(n / p)
        i += 1
    return divs
trianglenumbers = {1:1,2:3,3:6}
for i in range(4,100000):
    trianglenumbers[i] = trianglenumbers[i - 1] + i
    print(i, trianglenumbers[i])
ndiv = 0
##for j in range(1000,len(trianglenumbers)):
##    ndivt = len(pdiv(trianglenumbers[j]))
##    print(trianglenumbers[j],pdiv(trianglenumbers[j]))
##    if ndivt > 500:
##        print(trianglenumbers[j])
    
        
