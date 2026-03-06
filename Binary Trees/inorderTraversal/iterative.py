# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            # process node
            current = stack.pop()
            res.append(current.val)
            current = current.right
        return res

        