def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

def primefactors(n):
    lis = primes_sieve1(int(n / 5))
    primefacts = ""
    for i in lis:
        while n % i == 0:
            primefacts += str(i) + ' * '
            n /= i
    primefacts = primefacts[0:-3]
    return primefacts
print(primefactors(13195))
