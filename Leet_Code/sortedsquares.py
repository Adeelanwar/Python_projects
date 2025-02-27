def sortedSquares(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        newlist = [0 for i in nums]
        i = 0
        j = len(nums) - 1
        index = len(nums) - 1
        while (j >= i):
            if nums[j]**2 >= nums[i]**2:
                print(i, j, nums[i], nums[j])
                newlist[index] = nums[j]**2
                j -= 1
                print(index, newlist)
                index -= 1
            else:
                print(i, j, nums[i], nums[j])
                newlist[index] = nums[i]**2
                i += 1
                print(index, newlist)
                index -= 1
        return newlist
print(sortedSquares([-7,-3,2,3,11]))