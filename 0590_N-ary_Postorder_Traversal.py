"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    # Recursive
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        self.recurse(root, result)
        return result

    def recurse(self, root: 'Node', result: List[int]):
        if root is None:
            return

        for c in root.children:
            self.recurse(c, result)

        result.append(root.val)

    # Iterative
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = []
        stack_1 = [root]
        stack_2 = []

        while len(stack_1) > 0:
            node = stack_1.pop()
            stack_2.append(node)

            for c in node.children:
                stack_1.append(c)

        while len(stack_2) > 0:
            node = stack_2.pop()
            result.append(node.val)

        return result
