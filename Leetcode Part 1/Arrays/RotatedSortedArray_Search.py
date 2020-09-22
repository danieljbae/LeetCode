# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 01:13:06 2020

@author: danie
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Binary Search O(log n)
        low = 0
        high = len(nums)-1
        
        while low <= high: 
            mid = (low + high)//2
            
            # Target found
            if nums[mid] == target:
                return mid      
            # Rotated array logic - is this mid to high portion of the array sorted (not rotated) 
            # If mid to high portion (right) of array is sorted, then Binary search in this portion 
            elif nums[mid] <= nums[high]: 
                if nums[mid] < target <= nums[high]: # if our target value is between head or tail of sorted sublist, "rule out" low to mid 
                    low = mid + 1 
                else: # Target is not in the range of the mid to high  
                    high = mid - 1 
            
            # Rotated array logic - is this low to mid portion of the array sorted (not rotated) 
            # If low to mid (left) of array is sorted, then Binary search in this portion
            elif nums[mid] >= nums[low]: 
                if nums[low] <= target < nums[mid]: # if our target value is between head or tail of sorted sublist, "rule out" mid to high 
                    high = mid - 1 
                else: # Target is not in the range of the low to mid  
                    low = mid + 1
        return -1


nums = [4,5,6,7,0,1,2]
target = 0
test = Solution()

print(test.search(nums,target))