def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        kitems = nums[-1: -k - 1: -1]
        print(kitems)
        for i in range(len(nums) - k):
            nums[-i - 1] = nums[-i - k - 1]
        nums[:k] = kitems[-1::-1]
        return nums
print(rotate([1,2,3,4,5,6,7],3))
print(rotate([-1,-100,3,99],2))