class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 1: 
            return ""
        
        start, end = 0, 0 
        
        # iterates over all possible "centers" of palindrone 
        for i in range(len(s)): 
            len_odd = self.expand_fromcenter(s, i, i) # odd substr - single center'd palindrone 
            len_even = self.expand_fromcenter(s, i, i+1) # even substr - double center'd palindrone
            len_max = max(len_even,len_odd)
            
            if (end-start < len_max): # update head and tail of longest substring
                start = i - ((len_max - 1)/2)
                end = i + (len_max/2)
            
        return s[start:end+1] 

        
        
        
        
        
    def expand_fromcenter(self, s, left, right):
        """
        Keeps on expanding left and right indices from center until 
        string is no longer a palindrone. Returns the legnth palindrone

        s: str - for which we are confirming 
        left: - idx of center, which expands left
        right - idx of center, which expands right
        return the legnth of longest palindrone
        """
        l = left
        r = right

        # while in bounds and is a palindrone expands left and right
        while (l >= 0) and (r < len(s)) and (s[r] == s[l]):
            l -= 1 
            r += 1 

        return r - l - 1 
        
        