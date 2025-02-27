from Prime import sieve

def isPrime(n):
    if n == 1: return False
    else:
        if n < 4: return True
        else:
            if n % 2 == 0: return False
            else:
                if n < 9: return True 
                else:
                    if n % 3 == 0: return False
                    else:
                        r = int( n**(.5) )
                        f = 5
                        while f <= r:
                            if n % f == 0: return False 
                            if n %(f+2) == 0: return False
                            f = f + 6
    return True

val = 1
j = 1
k = 0
inc = 2
count = 0
while(1):
    k += 1
    for i in range(4):
        val += inc
        j += 1
        if isPrime(val) == True:
            count += 1
    inc += 2
    if count / j < .1:
        print(k, 1 + 2 * k)
        break
        
