# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root) -> int:
        if not root:
            return -1
        self.result = float('inf')
        min_val = root.val

        def dfs(node):
            if not node:
                return
            if min_val < node.val < self.result:
                