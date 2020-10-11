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
        # BFS - Iterative, Que 
        
        if not root: # Base case
            return root
        
        ret = []  # list for all nodes
        que = [root] # intialize, que helps us as FIFO emulates BFS/level order logic
        
        while que: # iterate until we have traversed all nodes
            level = [] # collects nodes for each level
             
            layer_size = len(que)
            for i in range(layer_size): # iterates all nodes on a given level, len(que)
                cursor = que.pop(0) 
                level.append(cursor.val)

                # drives layer size variable 
                if cursor.left: 
                    que.append(cursor.left) 
                if cursor.right:
                    que.append(cursor.right) 
                    
            ret.append(level) # level completed, add given level's nodes to result 
        return ret
            
        