# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 01:24:33 2020

@author: danie
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums)) 
    
test = Solution()
nums = [1,2,3,1]
print(test.containsDuplicate(nums))
