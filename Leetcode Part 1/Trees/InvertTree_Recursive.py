# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Recursive Approach
        
        
        if not root: # Base case - once bottom of tree reached
            return None
        
        left = self.invertTree(root.left) # recurse - downwards to left, return children
        right = self.invertTree(root.right) # recurse - downwards to right, return children
        
        # Swap
        root.left = right 
        root.right = left 
        
        return root # return upwards, after we have swapped
        