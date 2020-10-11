# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper_validate(root,float('inf'),float('-inf'))
    
    def helper_validate(self, root, max, min):
        """
        :type root: TreeNode - Current node (left/right child)
        :type max: int - Left Child's Ancestor value  
        :type min: int - Right Child's Ancestor value
        
        """
        if not root: # base case - leaf nodes reached 
            return True 
        
        elif (max <= root.val) or (min >= root.val): # base case - BST Invariant broken 
            return False
        
        else: # recursive call - continue traversing
            return self.helper_validate(root.left, root.val, min) and self.helper_validate(root.right, max, root.val)
        