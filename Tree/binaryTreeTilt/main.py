# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        self.totalTilt = 0
        def dfs(node) ->int:
            if not node:
                return 0
            leftsum = dfs(node.left)
            rightsum = dfs(node.right)

            self.totalTilt += abs(rightsum-leftsum)
            return leftsum + rightsum + node.val
        dfs(root)
        return self.totalTilt