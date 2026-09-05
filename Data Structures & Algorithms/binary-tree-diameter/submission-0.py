# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            # helper returns (length without arrow tip, length with arrow tip)
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            return (1 + max(left[0], right[0]), max(left[1], right[1], left[0] + right[0]))
        return helper(root)[1]