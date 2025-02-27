def ispal(string):
    if len(string) >= 1:
        if string[0] == string[-1]:
            return ispal(string[1:-1])
        else:
            return False
    else:
        return True
for i in range(1000,900,-1):
    for j in range(1000,900,-1):
        if ispal(str(i * j)):
            print(i, j, i * j)
            break
