# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # Recursive
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None

        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    # Iterative
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None

        node = root
        while node is not None:
            if node.val == val:
                return node
            elif val < node.val:
                node = node.left
            else:
                node = node.right

        return None
