def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        Memo = [[1], [1, 1]]
        i = 1
        leng = 3
        while (i < numRows):
            lst = [0] * leng
            lst[0] = 1
            lst[leng - 1] = 1
            for j in range(1, leng - 1):
                lst[j] = Memo[i][j - 1] + Memo[i][j]
            Memo.append(lst)
            leng += 1
            i += 1
        return Memo
print(generate(100))