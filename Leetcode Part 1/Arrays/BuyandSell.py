# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:32:48 2020

@author: danie
"""

# Time: O(n), beats 84.07% - single pass 
# Space: O(n), beats 11.60% - no additional structures needed


class Solution:
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minBuyprice = float('inf') # Intialize min buy price, such that any intial price will set value
        maxProfit = 0  # Intialize profit, such that a subsequent sell price must be greater than buy price  

        for price in prices:
            if price < minBuyprice: # if lower price found, then update min Buy price  
                minBuyprice = price
            elif price - minBuyprice > maxProfit: # if greater proft found, then update profit
                maxProfit = price - minBuyprice
        
        
        return maxProfit
        # suppose we have prices [7,2,5,3,6,4,1,1]
        # with this approach the min Buy price would be updated from: $2 into $1
        # However, this update is not problematic because 
        # Our profit will not be updated, 
        # as current Price ($1) and the new minimum buy price ($1), gives us a profit of $0 
        # which is less than 


prices = [7,2,5,3,6,4,1,1]

test = Solution()
print(test.maxProfit(prices))