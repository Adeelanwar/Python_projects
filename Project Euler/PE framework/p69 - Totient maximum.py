from NT import phi
from Prime import sieve
x = sieve(10**3)
number = 1
for i in x:
    if number * i <= 10**6:
        number *= i
    else:
        break
z = phi(number)
print(number, z ,number / z)
