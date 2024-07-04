# second way leetcode
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        node = root
        if node is None:
            return 0
        else:
            left_depth = self.maxDepth(node.left)
            right_depth = self.maxDepth(node.right)
            return max(left_depth, right_depth) + 1