def near(k = 2 * 10**6):
    nearest = (0,0)
    neardis = 10000000
    area = 0
    neararea = 0
    for m in range(20,1000):
        for n in range(m, 1000):
            z = int((m)*(m + 1)*(n)*(n + 1) / 4)
            if abs(z - k) < neardis:
                neardis = abs(z - k)
                nearest = (m , n)
                area = m * n
                nearestarea = z
    print(nearest, neardis,area, z)
near()
        
