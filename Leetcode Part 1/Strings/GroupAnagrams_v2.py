# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:38:46 2020

@author: danie
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        
        default_map = defaultdict(list) 
        for word in strs:
            key = [0] * 26 # use an array/tuple as key to standardize keys
            for char in word:
                key[ord(char) - ord("a")] += 1 # use "a" as baseline such that we have a range from 0-25
            default_map[tuple(key)].append(word) # convert array into tuple 
        
        return list(default_map.values())
        
        
    

strs = ["eat","tea","tan","ate","nat","bat"]
test = Solution()

print(test.groupAnagrams(strs))