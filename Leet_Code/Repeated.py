def repeatedSubstringPattern( s):
    """
    :type s: str
    :rtype: bool
    """
    length = len(s)
    mid = int((length - 1) / 2)
    for i in range(mid + 1):
        
        if length % (i + 1) == 0:
            ratio = int(length / (i + 1))
            substr = s[:i + 1]
            substr = s[:i + 1] * ratio
            if substr == s:
                return True
            
    return False

print(repeatedSubstringPattern('abab'))
print(repeatedSubstringPattern('ababa'))