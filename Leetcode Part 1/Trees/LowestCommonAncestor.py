# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Iterative Approach - O(n) time and space
        curr = root
        while curr:
            
            # Nodes p and q are in left subtree -> recurse downwards left
            if (p.val < curr.val) and (q.val < curr.val):
                curr = curr.left
                
            # Nodes p and q are in left subtree -> recurse downwards left
            elif (p.val > curr.val) and (q.val > curr.val):
                curr = curr.right

            # Nodes p and q are split - between left and right subtree
            # -> return current node, as this must be the lowest possible node
            else: 
                return curr 
        
        