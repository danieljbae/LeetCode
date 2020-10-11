# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        
        while True:
            while root: 
                stack.append(root)
                root = root.left # recurse left
            
            root = stack.pop() # return data
            k -= 1
            if not k: # "not" operator is faster than "k == 0"
                return root.val
            root = root.right # recurse right
            
        
        
        