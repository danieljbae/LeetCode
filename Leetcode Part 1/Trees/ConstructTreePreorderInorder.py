# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 
        if inorder: 
            # index in the inorder list, acting as partition of subtrees
            # pop values in pre order, as they are sorted by levels
            root_idx = inorder.index(preorder.pop(0)) 
            root_node = TreeNode(inorder[root_idx]) # allocate memory
            
            root_node.left = self.buildTree(preorder,inorder[0:root_idx]) # recurse and pass in left subtree
            root_node.right = self.buildTree(preorder,inorder[root_idx+1:]) # recurse and pass in right subtree
            
            return root_node
            
            