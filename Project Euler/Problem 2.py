Memo = {0:0,1:1}
def fib(n):
    if n in Memo:
        return Memo[n]
    if n > 1:
        fn = fib(n - 1) + fib(n - 2)
        
        Memo[n]= fn
        return fn
for i in range(1,100):
    fib(i)
    if Memo[i - 1] > 4000000:
        break
totalsum = 0
for j in range(3,i+1,3):
    totalsum += Memo[j]
    print (j, Memo[j], totalsum)
print(totalsum)
