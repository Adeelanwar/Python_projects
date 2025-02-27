fib = [0, 1]
for i in range(1,201):
    fib.append(fib[i] + fib[i - 1])
index = 3
sumt = 0
while (fib[index] <= 4 * 10**6):
    sumt += fib[index]
    index += 3

print(index, sumt)
