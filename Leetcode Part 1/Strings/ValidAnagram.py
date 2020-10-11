class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        str_frq = {}
        
        # initialize hash table to count freq of chars
        for s_char in s:
            if s_char in str_frq:
                str_frq[s_char] += 1 
            else:
                str_frq[s_char] = 1
        
        # update hash table to reduce count freq to zero 
        for t_char in t:
            if t_char in str_frq:
                str_frq[t_char] -= 1 
            else:
                str_frq[t_char] = 1
        
        # Check if all key,val are zero
        for key,val in str_frq.items():
            if val != 0:
                return False # if not, then it is not valid annogram=
        return True
        
            
            