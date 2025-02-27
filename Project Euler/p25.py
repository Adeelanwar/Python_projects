for n in range(100,1000):
    a = 1 + (5)**(1 / 2)
    b = 1 - (5)**(1 / 2)
    c = (a ** n - b ** n) / (2**n * 2.2)
    print (n, c)
