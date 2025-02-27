totalsum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        totalsum += i
        print(i , end = ", ")
print("\n" + str(totalsum))
    
