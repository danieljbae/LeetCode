# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 00:15:25 2020

@author: danie
"""

class Solution(object):        
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Dynamic Programming Approach O(n) - Kadane's Algo
        
        # Memo Table that will store the global solution at every index
        ans = [0]*len(nums) # Create Memo Table
        ans[0] = nums[0] # Initialize Memo Table
    
        # Single pass will update every index with optimal solution
        # Start @ 1 already intialized this value, this is critical in DP as we need to reference previous solutions
        for i in range(1,len(nums)):   
            ans[i] = max(nums[i], ans[i-1]+nums[i]) # Decision: cut off exiting solution/subarray as new element found is more optimal, extend sub array with new element found  
        return max(ans)
            
            
            
            
            
nums = [-2,1,-3,4,-1,2,1,-5,4]
test = Solution()
print(test.maxSubArray(nums))
            
            
            
            
            
        