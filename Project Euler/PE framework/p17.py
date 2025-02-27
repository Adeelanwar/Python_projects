def count(n):
    if n == 0: return 0
    if n in [1,2,6,10]: return 3
    if n in [4,5,9]: return 4
    if n in [3,7,8,50,60,90]: return 5
    if n in [11,12,20,30,40,80]: return 6
    if n in [15,16,70]: return 7
    if n in [13,14,18,19]: return 8
    if n == 17: return 9
    if n == 1000: return 11
    if n < 100: return count(n - n % 10) + count(n % 10)
    if n >= 100:
        if n % 100 != 0: return count(int(n / 100)) + 10 + count(n % 100)
        else: return count(int(n / 100)) + 7
value = 0
for i in range(1,1001):
    value += count(i)
print(value)
