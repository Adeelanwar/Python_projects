import math as m
def sieve(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

primes1000 = sieve(10**3)
primes = sieve(10**5)
maxcounter = 0
for b in primes1000:
    for a in range(-999,1000):
        n = 0
        count = 0
        while (1):
            z = n**2 + a * n + b
            if z in primes:
                n += 1
            else:
                if n > maxcounter:
                    print(a, b, n)
                    maxcounter = n
                break
