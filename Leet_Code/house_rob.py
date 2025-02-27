def rob(nums):
    Memo = {0: nums[0]}
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    if n == 3:
        return max(nums[2] + nums[0], nums[1])
    if n > 2:
        Memo[1] = max(nums[0], nums[1])
        Memo[2] = max(nums[2] + nums[0], nums[1])
    i = 3
    while(i < n):
        Memo[i] = max(nums[i] + Memo[i - 2], nums[i - 1] + Memo[i - 3])
        i += 1
    print(Memo)
    return Memo[n - 1]

print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))
print(rob([4,1,2,7,5,3,1]))
