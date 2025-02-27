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
under10 = [3, 5, 7, 11, 13]
under100 = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
callist = [(i**2 + 13) / 2 for i in under100]
print(callist)

for q in callist:
    found = 0
    for m in range(2, int(q / 3) + 2):
        for n in range(m + 1, int(q) + 2):
            if (3*m + n) == q:
                found += 2
    findings.append(found)
print(findings)
##for i in range(1,len(findings)):
##    findings[i] -= findings[i - 1]
##print(findings)
##ts = 0
##for j in (findings):
##    ts += j
##print(ts)
