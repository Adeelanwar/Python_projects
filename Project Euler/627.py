tn = 0
pairs = []
for i in range(1,30):
    for j in range(1,30):
        if i * j <= 9:
            tn += 1
            pairs.append((i,j))

print (tn)
print (pairs)
