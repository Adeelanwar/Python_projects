def gcd(a, b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b) 


def ETF(n):
    count = 0;
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count

def phi(n) :
 
    result = n   # Initialize result as n
      
    # Consider all prime factors
    # of n and for every prime
    # factor p, multiply result with (1 - 1 / p)
    p = 2
    while(p * p<= n) :
 
        # Check if p is a prime factor.
        if (n % p == 0) :
 
            # If yes, then update n and result
            while (n % p == 0) :
                n = n // p
            result = result * (1.0 - (1.0 / (float) (p)))
        p = p + 1
         
         
    # If n has a prime factor
    # greater than sqrt(n)
    # (There can be at-most one
    # such prime factor)
    if (n > 1) :
        result = result * (1.0 - (1.0 / (float)(n)))
  
    return (int)(result)

def caletf(n):
    TS = 1
    for i in range(2, n + 1):
        TS += phi(i)
    return TS
def ishamming(n):
    if n > 1:
        if n % 2 == 0:
            return ishamming(n / 2)
        if n % 3 == 0:
            return ishamming(n / 3)
        if n % 5 == 0:
            return ishamming(n / 5)
        else:
            return False
    if n == 1:
        return True
print(ishamming(6))
def cal(n):
    TS = 1
    for i in range(2, n + 1):
        if ishamming(phi(i)):
            TS += i
    return TS
print(cal(100))
