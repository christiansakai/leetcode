# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # Recursive
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        self.recurse(root, result)
        return result

    def recurse(self, root: TreeNode, result: List[int]) -> List[int]:
        if root is None:
            return

        self.recurse(root.left, result)
        self.recurse(root.right, result)
        result.append(root.val)

    # Iterative Two Stack
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        result = []

        stack_1 = [root]
        stack_2 = []

        while len(stack_1) > 0:
            node = stack_1.pop()
            stack_2.append(node)

            if node.left:
                stack_1.append(node.left)

            if node.right:
                stack_1.append(node.right)

        while len(stack_2) > 0:
            node = stack_2.pop()
            result.append(node.val)

        return result
