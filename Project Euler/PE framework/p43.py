def check(num):
    if len(num) <= 1:
        return False
    if len(num) == 2:
        if num[0] == num[1] or num[0] == 0 or num[1] == 0:
            return False
        else:
            return True
    else:
        if num[0] != num[1] and num[2] != num[1] and num[2] != num[0]:
            return True
        else:
            return False
       
list2 = [i for i in range(10,1000,2) if check(str(i)) == True]
list5 = ([i for i in range(10,1000,5) if check(str(i)) == True])
list17 = ([i for i in range(10,1000,17) if check(str(i)) == True])

