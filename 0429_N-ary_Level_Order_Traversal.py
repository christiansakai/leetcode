"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = [root]

        while len(queue) > 0:
            qlen = len(queue)
            level = []

            for i in range(0, qlen):
                node = queue.pop(0)
                level.append(node.val)

                for c in node.children:
                    queue.append(c)

            result.append(level)

        return result
