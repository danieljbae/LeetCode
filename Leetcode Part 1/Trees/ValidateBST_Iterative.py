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
        # iterative solution
        
        if not root: return True 
        
        # intialize stack - left and right  
        stack = [(root, -float('inf'), float('inf'))]
        
        while stack:
            cursor,left,right = stack.pop() # left represents left child (cursor) parent's value
            if cursor.val <= left or cursor.val >= right: 
                return False
            
            if cursor.left:
                stack.append((cursor.left,left, cursor.val))
            
            if cursor.right:
                stack.append((cursor.right,cursor.val, right))
            
        return True
                
            
        
        