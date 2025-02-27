result = 0
for i in range(1,101):
    for j in range(i + 1,101):
        if i != j:
            result += 2 * i * j
