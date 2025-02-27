num = set([])
for a in range(2, 100 + 1):
    for b in range(2,100 + 1):
        num.add(a**b)
print(len(num))
