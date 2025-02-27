for i in range(1,100000):
    a = i*(2*i - 1)
    k = (1 + 24 * a)**(1/2)
    l = (1 + 8 * a)**(1/2)
    if k % 1 == 0 and l % 1 == 0:
        t = (1 + k)/ 6
        u = (-1 + l) / 2 
        if t % 1 == 0 and u % 1 ==0:
            print(i, t, u, a)
            
    
