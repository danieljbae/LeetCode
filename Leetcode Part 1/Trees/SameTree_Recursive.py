# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # Iterative Approach 
        
        stack = [(p,q)]
        
        while stack:
            p_curr, q_curr = stack.pop() 
            
            if (not p_curr) and (not q_curr): # Base case - both nodes are null 
                continue  
                
            if (not p_curr) or (not q_curr): # Base case - one of P or Q is null
            
            # if (not p_curr and q_curr) or (p_curr and not q_curr): # Base case - one of P or Q is null
                return False

            if p_curr.val != q_curr.val: # Base case - nodes do not have matching values 
                return False
            
            # Iterate downwards using Stack
            # we add the next layer of tree, in pairs of the same branch (left/left) or (right/right) 
            stack.append((p_curr.left,q_curr.left))
            stack.append((p_curr.right,q_curr.right))

        return True # by finishing Loop, we can conclude we have same tree 
        
        
                
        