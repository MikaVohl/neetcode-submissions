# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if not node:
                return 0
            l = height(node.left)
            r = height(node.right)
            if abs(l - r) > 1 or l == 0 and node.left or r == 0 and node.right:
                return 0
            return max(l, r) + 1

        return not (height(root) == 0 and root)