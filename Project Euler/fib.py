import sys

def fib(n):
    if n == 1:
        return 1
    elif n <= 0:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)
def dynfib(n,memo = {0 : 0, 1 : 1}):
    if memo.get(n) == None:
        print(n)
        memo[n] = dynfib(n - 1,memo) + dynfib(n - 2,memo)
    return memo[n]
def dfib(n):
    memo = {0 : 0, 1 : 1}
    for i in range(n):
        print(dynfib(i + 1,memo))
sys.setrecursionlimit(100000)
dfib(50)
print(fib(50))
