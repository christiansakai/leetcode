"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        if len(root.children) == 0:
            return 1

        maximum = 0
        for c in root.children:
            sub_prob = self.maxDepth(c)
            maximum = max(maximum, sub_prob)

        return maximum + 1
