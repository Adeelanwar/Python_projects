def spiral(n):
    m = int(n / 2) + 1
    num = 1
    inc = 2
    totalsum = 1
    for i in range(1, m):
        for j in range(4):
            num += inc
            totalsum += num
        inc += 2
    return(totalsum)
print(spiral(1001))
        
    
