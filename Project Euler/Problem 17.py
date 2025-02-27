dletter = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,9,8,6]
dletter10 = [6,6,5,5,7,7,6,7]
dletter100 = [10,10,12,11,11,10,12,12,11,11]

total = 0
for j in range(10):
    for i in range(1,100):
        if j >= 1:
            total += dletter100[j] + 3
        if i <= 20:
            total += dletter[i]
        elif i > 20 and i < 100: 
            ones = i % 10
            total += dletter10[int(i / 10) - 2] + dletter[ones]
    total += dletter100[j]
total += 11
print(total)
