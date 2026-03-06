# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        def dfs(node,isLeftChild):
            if not node:
                return 0
            if not (node.left or node.right): # leaf
                return node.val if isLeftChild else 0
            return dfs(node.left,True) + dfs(node.right,False)
        return dfs(root,False)
        

        