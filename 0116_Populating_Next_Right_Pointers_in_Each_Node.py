"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    # Iterative
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        queue = [root]
        while len(queue) > 0:
            qlen = len(queue)

            for i in range(0, qlen):
                node = queue.pop(0)
                if i < qlen - 1:
                    node.next = queue[0]

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root
