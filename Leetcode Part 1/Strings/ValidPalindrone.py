class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Double Pointer approach O(n)
        
        # Base case
        if len(s) == 0:
            return True 
        
        # Intializing Double pointers
        i = 0
        j = len(s) - 1
        
        while i < j:
            # Each char must be alpha num in order to perform a valid equality comparision 
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower(): # if they are equal, continue to check if it is a palimdrone
                    i += 1 
                    j -= 1
                else: 
                    return False
                
            # Individually check each pointer, such that each pointer can be adjusted independently 
            else:
                if not (s[i].isalnum()): 
                    i += 1
                if not (s[j].isalnum()):
                    j -= 1
        return True # full pass, so it is a palimdrone