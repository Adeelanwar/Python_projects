from Prime import sieve
primes = sieve(10**6)
listfact = [0, 1]
def fact(n):
    i = 2
    while (i <= n):
        listfact.append(i * listfact[i - 1])
        i += 1
numbers = [True] * 10**8

