day = 2
sjun = 0
daysinmonth = [31,28,31,30,31,30,31,31,30,31,30,31]
daysinmonthl = [31,29,31,30,31,30,31,31,30,31,30,31]
for i in range(1,101):
    if i % 4 == 0:
        for j in daysinmonthl:
            day = (day + j) % 7
            if day == 0:
                sjun += 1
    else:
        for j in daysinmonth:
            day = (day + j) % 7
            if day == 0:
                sjun += 1
print(sjun)
