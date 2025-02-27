def WTOA(word):
    value = 0
    for i in word:
        value += ord(i) - ord('@')
    return value
file = open('p022_names.txt','r')
string = ''
for i in file:
    string += i
string2 = ''
for j in string:
    if j != '"':
        string2 += j 
listofwords = string2.split(',')
listofwords.sort()
print(listofwords[937])
total_value = 0
for i in range(1, len(listofwords) + 1):
    value = i * WTOA(listofwords[i - 1])
    total_value += value
print(total_value)
