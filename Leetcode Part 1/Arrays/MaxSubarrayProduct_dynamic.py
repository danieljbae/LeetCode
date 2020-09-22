# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 02:29:06 2020

@author: danie
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        ex. [-2,3,-4] -> 24
        """
        if len(nums) == 1:
            return nums[0]
            
        current_max = nums[0]
        current_min = nums[0]
        final_max = nums[0]
        
        for i in range(1,len(nums)):
            
            temp_current_max = current_max # Store current max as it may be updated due to a new element found or an extenstion 
            current_max = max(nums[i],max(current_max*nums[i],current_min*nums[i])) # Store the most positive product at a given index
            current_min = min(nums[i],min(temp_current_max*nums[i],current_min*nums[i])) # Store the most negative product at a given index
                                                                    # Updating our minimum allows us to capture large negative numbers
                                                                    # By storing the most negative number, we can we can 
                                                                    # use dynamic programming to reference a previous solution
            # update our final max if we have found 
            if current_max > final_max:
                print(final_max)
                final_max = current_max
                print(final_max)
        
        return final_max
            