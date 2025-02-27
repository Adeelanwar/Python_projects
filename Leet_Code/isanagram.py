def isAnagram(s, t):
        chartonum = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19,
                     'i': 83, 'j': 89, 'k': 23, 'l': 29, 'm': 31, 'n': 37, 'o': 41, 'p': 43,
                     'q': 47, 'r': 53, 's': 59, 't': 61, 'u': 67, 'v': 71, 'w': 73, 'x': 79,
                     'y': 97, 'z': 101}
        number1 = 1
        number2 = 1
        for i in s:
            number1 *= chartonum[i]
        for j in t:
            number2 *= chartonum[j]
        return number1 == number2