"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        head = self.recurse(root)
        tail = head

        while tail and tail.right:
            tail = tail.right

        tail.right = head
        head.left = tail

        return head

    def recurse(self, root: 'Node') -> 'Node':
        if root.left is None and root.right is None:
            return root

        if root.left and root.right:
            left = self.recurse(root.left)
            right = self.recurse(root.right)

            left_tail = left
            while left_tail and left_tail.right:
                left_tail = left_tail.right

            left_tail.right = root
            root.left = left_tail

            root.right = right
            right.left = root

            return left

        if root.left:
            left = self.recurse(root.left)

            left_tail = left
            while left_tail and left_tail.right:
                left_tail = left_tail.right

            left_tail.right = root
            root.left = left_tail

            return left

        right = self.recurse(root.right)
        root.right = right
        right.left = root

        return root
