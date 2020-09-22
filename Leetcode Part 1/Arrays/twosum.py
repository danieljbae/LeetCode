# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 20:57:07 2020

@author: danie
"""
# Question: https://leetcode.com/problems/two-sum/





diff_dict = {}

class Solution: 
    
    def twoSum(self, nums,target):
        diff_dict = {} # stores keys as target - element, 
                       # and value as index in nums list 
        
        for key,val in enumerate(nums):
            if val in diff_dict: # if remaining: intialized in dict and is contained in nums list
                return ([diff_dict[val],key]) 
            else: # intializing keys with remaining values
                diff_dict[target-val] = key 


nums = [7,2,15,17]
target = 9

test = Solution()
print(test.twoSum(nums,target))

