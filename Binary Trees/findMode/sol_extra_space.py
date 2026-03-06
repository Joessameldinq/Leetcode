# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root) -> list[int]:
        dict = {}
        def dfs(node):
            if not node:
                return
            val = node.val
            if val in dict:
                dict[val] += 1
            else:
                dict[val] = 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        max_val = max(dict.values())
        return [n for n in dict if dict[n] == max_val]
        
        