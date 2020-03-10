# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if root is None or p is None:
            return None

        node = root
        stack = []
        p_found = False

        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if p_found:
                return node

            if p_found == False and p.val == node.val:
                p_found = True

            node = node.right

        return None
