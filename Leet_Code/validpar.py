def isValid(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(')')
        elif i == '{':
            stack.append('}')
        elif i == '[':
            stack.append(']')
        if i == ')':
            if i not in stack:
                return False
        if i == ']':
            if i not in stack:
                return False
        if i == '}':
            if i not in stack:
                return False
        if len(stack) >= 1:
            if i == stack[-1]:
                stack.pop(-1)
    if len(stack) == 0:
        return True
    return False