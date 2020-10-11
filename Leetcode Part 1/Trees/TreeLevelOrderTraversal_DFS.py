# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # DFS - Recurisve, Hash Map
        if not root:
            return root
            
        hashMap = collections.defaultdict(list) # keys = level idx, vals = [node values]
        level = 1 # intial level
        nodesMap = self.helper_Dfs(root, hashMap,level)
        return nodesMap.values()
        
        
        
    def helper_Dfs(self, node, hashMap,level):
        
        if node: 
            hashMap[level].append( node.val ) # use level as key and append values 
        
        # update level order through states of recursion 
        if node.left:
            self.helper_Dfs(node.left, hashMap, level+1)
        if node.right:
            self.helper_Dfs(node.right, hashMap, level+1)
        return hashMap
            
            
        