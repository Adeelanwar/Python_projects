def evalRPN(tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        symbols = {'+','-', '*','/'}
        Answer = 0
        i = 2
        while (len(tokens) > 2):
            if tokens[i] in symbols:
                print('tokens: ', tokens)
                tokens[i - 2] = int(eval(f'{tokens[i - 2]}{tokens[i]}{tokens[i - 1]}'))
                tokens.pop(i)
                tokens.pop(i - 1)
                print('after: ', tokens)
                i -= 1
            else:
                i += 1
        return tokens[0]
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))