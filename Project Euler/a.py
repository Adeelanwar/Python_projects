for i in range(1000):
    for j in range(i, 1000):
        k = 1000 - i - j
        if i**2 + j ** 2 == k**2:
            print (i * j * k)
            print (i, j, k)
            break
        
