import sys
memo = {1 : 1}
def collatz(n,length = 0):
    if memo.get(n) == None: 
        if n == 1:
            return length
        if n % 2 == 0:
            memo[n] = collatz(int(n / 2),length + 1) - length
            return memo[n] + length
        else:
            memo[n] = collatz(3 * n + 1,length + 1) - length
            return memo[n] + length
    else:
        return length + memo[n]
for i in range(1,10**6):
    collatz(i)
maxt = 0
for k,v  in memo.items():
    if maxt < v and k < 10**6:
        print(k, v)
        maxt = v
print(maxt)
