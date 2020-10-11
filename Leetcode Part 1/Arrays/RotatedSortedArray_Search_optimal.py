class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        piv = -1
        n = len(nums)
        maxv = float('-inf')
        
        # Find point of rotation
        for i in range(n):
            if nums[i] < maxv:
                piv = i
                break
            else:
                maxv = max(nums[i], maxv)
        
        # Fix rotated array
        nums_new = nums[piv:]+nums[:piv]       
        
        cur = target
        while 