def pennums(n):
    listpen = []
    for i in range(1, n + 1):
        listpen.append(int(i * (3 * i - 1) / 2))
    return listpen
listpen = pennums(1000)
print(pennums(10))
def fact(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
def ncr(n,r): return int(fact(n) / (fact(n - r) * fact(r)))
print(ncr(len(listpen), 2))

    
