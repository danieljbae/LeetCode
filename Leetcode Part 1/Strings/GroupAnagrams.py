# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 22:37:44 2020

@author: danie
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Time complexity - O(n k log k) 
        # Space complexity - O(nk)
        
        hash_map = {}
        for word in strs:
            key = tuple(sorted(word)) # converting each word into a key, such that each key standardized (ex. eat >> aet, ate >> aet) 
            if key in hash_map: 
                hash_map[key].append(word) # append each word to the list
            else: 
                hash_map[key] = [word] # intialize each value as a list format
        
        return list(hash_map.values())
    

strs = ["eat","tea","tan","ate","nat","bat"]
test = Solution()

print(test.groupAnagrams(strs))