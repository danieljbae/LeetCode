class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
         # intialize with closing brackets
        pair_map = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        if len(s) == 0: # string is legnth of zero is valid 
            return True
        elif len(s) % 2 or s[0] in pair_map: # odd number of brackets or start with closing bracket
            return False  
        
        # stack for opening brackets 
        stack = []
        # var to keep track of how many brackets we've opened and closed
        open_count = 0
        
        for char in s:
            # must be a closing bracket and Stack's top value must correspond to its open br  
            print(stack)
            if char in pair_map and (stack.pop() == pair_map[char]): 
                open_count -= 1 # reduce the number of brackets to close
                
            
            # openeing brackets
            else:
                stack.append(char) # add opening brackets in stack
                open_count += 1 # increase the number of brackets to close
        
        return not open_count # should be zero by end of algo
                
                