import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    min_diff = math.inf
    closest = math.inf
    
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.recurse(root, target)
        return self.closest
        
     
    def recurse(self, root: TreeNode, target: float):
        if root is None:
            return
        
        diff = abs(root.val - target)
        if diff < self.min_diff:
            self.min_diff = diff
            self.closest = root.val
            
        self.recurse(root.left, target)
        self.recurse(root.right, target)
            
