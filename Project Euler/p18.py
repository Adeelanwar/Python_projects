numbers = []
with open('p18.txt') as f:
    n = 0
    for line in f:
        numbers.append([])
        for i in range(0,len(line),3):
           numbers[n].append(int(line[i:i+2]))
        n += 1

for i in range(len(numbers)):
    pass
    
