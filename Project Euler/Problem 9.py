from math import sqrt
for a in range(1,1000):
    for b in range(a,1000 - a):
        c2 = a**2 + b**2
        c = int(sqrt(c2))
        if c**2 == c2:
            print(a, b, c, a**2, b**2, c**2, c2)
            if a + b + c == 1000:
                print(a, b, c, a * b * c)
                break
