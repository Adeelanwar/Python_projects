def divcount(div1, div2):
    for v in div1.key():
        pass
listfact =[1, 1]
def fact(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
def zhi(n):
    divisors = {1: 1}
    index = 1
    while n % 2 == 0:
        if divisors.get(2) == None:
            divisors[2] = 1
        else:
            divisors[2] += 1
        n = int(n / 2)
    while(n > 1):
        index += 2
        while n % index == 0:
            if divisors.get(index) == None:
                divisors[index] = 1
            else:
                divisors[index] += 1
            n = int(n / index)
    return divisors

for n in range(3,10):
    if n % 2 == 0:
        divisorsn = zhi(int(n / 2))
        divisorsn1 = zhi(n + 1)
    else:
        divisorsn1 = zhi(int((n + 1) / 2))
        divisorsn = zhi(n)
    print(int((n) * (n + 1) / 2), divisorsn,divisorsn1)
x = zhi(36)
total_sum = 0
for v in x.values():
    total_sum += v
print(total_sum)
