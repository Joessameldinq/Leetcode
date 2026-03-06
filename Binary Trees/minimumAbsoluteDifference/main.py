# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root) -> int:
        self.mindiff = float('inf')
        self.prev = None

        def inOrder(node):
            if not node:
                return
            inOrder(node.left)

            if self.prev:
                self.mindiff = min(self.mindiff,abs(node.val- self.prev.val))
            self.prev = node
            inOrder(node.right)
        