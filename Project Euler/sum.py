file = open('sum.txt','r')
totalsum = 0
for line in file:
    totalsum += int(line)


def fact(n):
    if n > 1:
        return n * fact(n - 1)
    else:
        return 1
x = str(fact(100))
tsum = 0
for i in x:
    tsum += int(i)
print(tsum)
