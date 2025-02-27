def minCostClimbingStairs(cost):
        n = len(cost)
        if n == 2:
            return min(cost[-1], cost[-2])
        Memo = {1: cost[-1]}
        Memo[2] = min(cost[-1], cost[-2])
        Memo[3] = min(cost[-3] + cost[-1], cost[-2])
        i = 3
        while(i < n):
            i += 1
            Memo[i] = min(cost[i * -1] + Memo[i - 1], cost[i * -1] + Memo[i - 2])
        print(Memo)
        return Memo[n]
print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print(minCostClimbingStairs([0,0,1,1]))