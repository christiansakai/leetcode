# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # Recursive
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        self.recurse(root, result)
        return result

    def recurse(self, root: TreeNode, result: List[int]):
        if root is None:
            return

        self.recurse(root.left, result)
        result.append(root.val)
        self.recurse(root.right, result)

    # Iterative
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = []

        while root is not None or len(stack) > 0:
            while root is not None:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)

            root = root.right

        return result
