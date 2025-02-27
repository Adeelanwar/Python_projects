spiral = 1001
diagonals = int(spiral / 2) + 1
count = 1
total = 1

for i in range(1, diagonals):
    step = 2 * i
    for j in range(1,5):
        count += step
        total += count 
        
