sumt = 0
with open('p13.txt') as f:
    n = 0
    for line in f:
        print(int(line[:-1]))
        sumt += int(line[:-1])
print(sumt)
