def fact(n):
    val = 1
    for i in range(2,n + 1, 1):
        val *= i
    return val
x = 10**6 - 2 * fact(9)
y = x - 6 * fact(8)
z = (y - 6 * fact(7))
k = (z - 2 * fact(6))
l = (k - 5 * fact(5))
m = (l - fact(4))
n = (m - 2 * fact(3))
print(n)
