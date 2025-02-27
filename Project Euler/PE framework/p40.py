number = ''
for i in range(1,1000001):
    number += str(i)
ans = 1
for j in range(1,7):
   ans *= int(number[10**j - 1])
print(ans)
