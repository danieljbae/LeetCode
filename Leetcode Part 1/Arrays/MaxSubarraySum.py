# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 00:14:08 2020

@author: danie
"""

class Solution(object):        
        
    def helper_mss(self,ls, l, r):
        
        # Divide and Conquer Approach: O(nlogn)
        # In general, divide and conquer algorithms willbe driven by recursion and a base case
        
        # base case
        if l == r:
            return ls[l]

        # mid point
        mid = (l+r)//2

        # recursion - each recursion call changes window capacity size
        left_ans = self.helper_mss(ls,l,mid)
        right_ans = self.helper_mss(ls,mid+1,r)

        ################################################
        #### Logic specific to this problem

        # find max contiguous sub array sum, left of pivot (mid)
        left_max = float('-inf') 
        sumVar = 0
        for i in range(mid,l-1,-1):
            sumVar += ls[i]
            left_max = max(left_max,sumVar)
            
        # find max contiguous sub array sum, right of pivot (mid)
        right_max = float('-inf') 
        sumVar = 0
        for i in range(mid+1,r+1,1):
            sumVar += ls[i]
            right_max = max(right_max,sumVar)

        return max(left_ans,right_ans,(left_max+right_max))
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper_mss(nums,0,len(nums)-1)
            
nums = [-2,1,-3,4,-1,2,1,-5,4]
test = Solution()
print(test.maxSubArray(nums))