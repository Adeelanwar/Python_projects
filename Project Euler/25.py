lfib = [1, 1]
def fib():
    n = 2
    while (n <= 10000 and len(str(lfib[-1])) < 1000):
        lfib.append(lfib[n - 1] + lfib[n - 2])
        n += 1
        print(n, len(str(lfib[-1])))
        
