# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True

        is_valid, _, _ = self.recurse(root)
        return is_valid

    def recurse(self, root: TreeNode) -> (bool, int, int):
        if root.left is None and root.right is None:
            return True, root.val, root.val

        curr_valid = True
        curr_small = root.val
        curr_big = root.val

        if root.left:
            left_valid, left_small, left_big = self.recurse(root.left)

            curr_valid = curr_valid and\
                root.val > root.left.val and\
                root.val > left_big and\
                left_valid

            curr_small = left_small

        if root.right:
            right_valid, right_small, right_big = self.recurse(root.right)

            curr_valid = curr_valid and\
                root.val < root.right.val and\
                root.val < right_small and\
                right_valid

            curr_big = right_big

        return curr_valid, curr_small, curr_big
