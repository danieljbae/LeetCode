# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 00:47:27 2020

@author: danie
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Binary Search Approach O(log n)
        left = 0
        right = len(nums)-1
        
        while left < right:
            
            # pivot index to determine if right half is in increasing order
            # in other words, this pivot determines if left/right half can be "ruled out"
            # by dividing our window within the array in 1/2, we will get O(log n) 
            mid = (left + right)//2 
            
            # inflection point is not contained in right half - bc right half is in increasing order
            if nums[mid] < nums[right]: 
                right = mid 
            
            # inflection point is contained in right half - bc right half is not in increasing order
            else: 
                left = mid+1
            
        return nums[left]
                

nums = [3,4,5,1,2] 
test = Solution()

print(test.findMin(nums))
            