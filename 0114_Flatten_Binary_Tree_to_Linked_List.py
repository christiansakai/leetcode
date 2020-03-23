# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.recurse(root)
        
    def recurse(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root

        left = self.recurse(root.left)
        right = self.recurse(root.right)
        
        if left is not None and right is not None:
            root.left = None
            root.right = left

            temp_left = left
            while temp_left is not None and temp_left.right is not None:
                temp_left = temp_left.right
                
            temp_left.right = right
        elif left is not None:
            root.left = None
            root.right = left
        else:
            root.left = None
            root.right = right
        
        return root
