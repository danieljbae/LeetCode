# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global_depth = [0]
        
        # DFS helper - update the maximum depth as we recurse to leaf nodes in left/right subtree
        def dfs_helper(node,level):
            global_depth[0] = max(level,global_depth[0])
            
            if node.left: # DFS - recurse downwards left, incrument level/depth by 1
                dfs_helper(node.left,level+1)
        
            if node.right: # DFS - recurse downwards right, incrument level/depth by 1
                dfs_helper(node.right,level+1)

        if root: # if we have valid tree, call dfs function
            dfs_helper(root,1) # pass in intial depth value of 1
            
        return global_depth[0]
            
        