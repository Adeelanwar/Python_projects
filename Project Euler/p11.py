numbers = [[]]
with open('p11.txt') as f:
    n = 0
    for line in f:
        numbers.append([])
        for i in range(0,len(line),3):
           numbers[n].append(int(line[i:i+2]))
        n += 1

def checknumber(point, maximum):
    x = point[0]
    y = point[1]
    print(x, y, maximum)
    if x >= 3: #left
        prod = numbers[y][x] * numbers[y][x - 1] * numbers[y][x - 2] * numbers[y][x - 3]
        if prod >= maximum:
            maximum = prod
        if y >= 3: #left
            prod = numbers[y][x] * numbers[y - 1][x - 1] * numbers[y - 2][x - 2] * numbers[y - 3][x - 3]
            if prod >= maximum:
                maximum = prod
        if y <= len(numbers[0]) - 4:
            prod = numbers[y][x] * numbers[y + 1][x - 1] * numbers[y + 2][x - 2] * numbers[y + 3][x - 3]
            if prod >= maximum:
                maximum = prod
    if x <= len(numbers[0]) - 4:
        prod = numbers[y][x] * numbers[y][x + 1] * numbers[y][x + 2] * numbers[y][x + 3]
        if prod >= maximum:
            maximum = prod
        if y >= 3: #left
            prod = numbers[y][x] * numbers[y - 1][x + 1] * numbers[y - 2][x + 2] * numbers[y - 3][x + 3]
            if prod >= maximum:
                maximum = prod
        if y <= len(numbers[0]) - 4:
            prod = numbers[y][x] * numbers[y + 1][x + 1] * numbers[y + 2][x + 2] * numbers[y + 3][x + 3]
            if prod >= maximum:
                maximum = prod
    if y >= 3: #left
        prod = numbers[y][x] * numbers[y - 1][x] * numbers[y - 2][x] * numbers[y - 3][x]
        if prod >= maximum:
            maximum = prod
        if x >= 3: #left
            prod = numbers[y][x] * numbers[y - 1][x - 1] * numbers[y - 2][x - 2] * numbers[y - 3][x - 3]
            if prod >= maximum:
                maximum = prod
        if x <= len(numbers[0]) - 4:
            prod = numbers[y][x] * numbers[y - 1][x + 1] * numbers[y - 2][x + 2] * numbers[y - 3][x + 3]
            if prod >= maximum:
                maximum = prod
    if y <= len(numbers[0]) - 4:
        prod = numbers[y][x] * numbers[y + 1][x] * numbers[y + 2][x] * numbers[y + 3][x]
        if prod >= maximum:
            maximum = prod
        if x >= 3: #left
            prod = numbers[y][x] * numbers[y + 1][x - 1] * numbers[y + 2][x - 2] * numbers[y + 3][x - 3]
            if prod >= maximum:
                maximum = prod
        if x <= len(numbers[0]) - 4:
            prod = numbers[y][x] * numbers[y + 1][x - 1] * numbers[y + 2][x - 2] * numbers[y + 3][x - 3]
            if prod >= maximum:
                maximum = prod
    return maximum
maximum = 0
for i in range(20):
    for j in range(20):
        maximum = checknumber((i, j), maximum)
##        if temp > maximum:
##            temp = maximum
##            print(i, j, maximum)
