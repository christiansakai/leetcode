"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    # Iterative
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = []
        stack = [root]

        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)

            for i in range(len(node.children) - 1, -1, -1):
                stack.append(node.children[i])

        return result

    # Recursive
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        self.recurse(root, result)
        return result

    def recurse(self, root: 'Node', result: List[int]):
        if root is None:
            return

        result.append(root.val)
        for c in root.children:
            self.recurse(c, result)
