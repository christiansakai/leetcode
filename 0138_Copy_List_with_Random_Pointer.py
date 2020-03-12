from typing import Dict

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        visited = {}
        return self.recurse(head, visited)

    def recurse(self, node: 'Node', visited: Dict['Node', 'Node']) -> 'Node':
        if node in visited:
            return visited[node]

        cloned = Node(node.val)
        visited[node] = cloned

        if node.next is not None:
            cloned.next = self.recurse(node.next, visited)

        if node.random is not None:
            cloned.random = self.recurse(node.random, visited)

        return cloned
