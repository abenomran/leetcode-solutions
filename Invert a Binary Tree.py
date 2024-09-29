# Easy
from typing import TreeNode, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.rInvert(root)
        
    def rInvert(self, root):
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.rInvert(root.left)
        self.rInvert(root.right)

        return root