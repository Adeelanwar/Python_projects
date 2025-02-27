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
primes = sieve(2*10**6)
sumt = 0
for i in primes:
    sumt += i
print(sumt)
