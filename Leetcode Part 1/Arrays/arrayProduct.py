# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:37:45 2020

@author: danie
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        # Array of products to left of i'th element O(n) 
        left_product = [0]*len(nums)
        left_product[0] = 1 
        for i in range(1,len(nums)): # Skip head, so start at 1
            left_product[i] = nums[i-1] * left_product[i-1]
        
        
        # Array of products to right of i'th element O(n) 
        right_product = [0]*len(nums)
        right_product[len(nums)-1] = 1
        for i in range(len(nums)-2,-1,-1): # Skip tail, so start at n-2
            right_product[i] = nums[i+1] * right_product[i+1]
            
            
        # output - array to contain list of all products except itself
        # We can use the following logic: the ith element will be a result 
        # of all the product of the elements to left of it and right of it
        answer = [0]*len(nums)              
        for i in range(0,len(nums)):
            answer[i] = (left_product[i]*right_product[i])

        return answer
                
    
    
nums = [1,2,3,4]
test = Solution()

print(test.productExceptSelf(nums))



