class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if not s: # base case - empty string
            return 0
        
        n = len(s)
        max_size = 1
        beg,end = 0, 1 # intial sliding window size
        
        sub_set = set(s[beg])
        
        while beg < n and end < n: # moving sliding window until end of S
            
            if s[end] in sub_set: # slide beg of window rightwards - if end is a dupe 
                sub_set.remove(s[beg])
                beg += 1
                
            else: # slide end of window rightwards - if end is unique
                sub_set.add(s[end])
                end += 1 
                
            max_size = max(max_size,end-beg) 
        return max_size
        
                
                
                
        