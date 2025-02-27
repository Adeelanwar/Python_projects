def F(a, b, c):
    for n in range(c,100000*c,c):
        z = (n**2 / a) + (n**2 / b) + c
        if (z % 1) == 0:
            return 3 * n**2
        z = ((n**2 + 1) / a) + (n**2 / b) + c
        if (z % 1) == 0:
            return 3 * n**2 + 1
        z = ((n**2 + 1) / a) + ((n**2 + 1) / b) + c       
        if (z % 1) == 0:
            return 3 * n**2 + 2
print(F(9,10,11))
