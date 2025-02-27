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
findings = []
under10 = [2, 3, 5, 7]
under100 = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
callist = [int((i**2 + 11) / 4) for i in under100]
print(callist)


for p in callist:
##    found = p - 4 + 1
##    findings.append(found)
    found =  (p - 5) / 2 + (p - 3) / 2
    findings.append(found)
ts = 0
for j in (findings):
    ts += j
print(ts)
