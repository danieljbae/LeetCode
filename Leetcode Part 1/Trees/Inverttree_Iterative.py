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
        # Iterative Approach
        if not root: return None 
        
        que = [root]
        
        while que:
            cursor = que.pop(0) # Remove the first in line/list (FIFO)
            
            # Swap left and right children
            cursor.left, cursor.right = cursor.right,cursor.left
            
            # add left/right children to que 
            if cursor.left:
                que.append(cursor.left) # Append children to end of line/list 
            
            if cursor.right:
                que.append(cursor.right) # Append children to end of line/list 
        
        return root
            
            