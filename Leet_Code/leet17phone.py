def letterCombinations(digits):

    d2s = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'],
            '5': ['j','k', 'l'], '6': ['m','n','o'], '7': ['p','q','r','s'],
            '8':['t','u','v'], '9':['w','x','y','z']} 
    def multiplylist(list1,list2):
        lists = []
        for string2 in list2:
            for string1 in list1:
                lists.append(string1 + string2)
        return lists
    if len(digits) == 0:
        return []
    currentlist = ['']
    for i in digits:
        diglist = d2s[str(i)]
        currentlist = multiplylist(currentlist, diglist)
    return currentlist

print(letterCombinations([4,2,5,2,9,9]))