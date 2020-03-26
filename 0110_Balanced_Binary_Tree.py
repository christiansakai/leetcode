from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        height, is_balanced = self.recurse(root)
        return is_balanced
        
    
    def recurse(self, root: TreeNode) -> Tuple[int, bool]:
        if root is None:
            return 0, True
        
        if root.left is None and root.right is None:
            return 1, True
        
        left_height, left_is_balanced = self.recurse(root.left)
        right_height, right_is_balanced = self.recurse(root.right)
        
        is_balanced = left_is_balanced and right_is_balanced and abs(left_height - right_height) <= 1
        
        height = 1 + max(left_height, right_height)
        
        return (height, is_balanced)
        
