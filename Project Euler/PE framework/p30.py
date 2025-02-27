total_value = 0
for i in range(1,10**6):
    x = str(i)
    value = 0
    for j in x:
        value += int(j)**5
    if value == i:
        total_value += i
print(total_value)
