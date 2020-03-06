# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.node = root
        self.stack = []

        while self.node is not None:
            self.stack.append(self.node)
            self.node = self.node.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        next_node = self.stack.pop()

        self.node = next_node.right
        while self.node is not None:
            self.stack.append(self.node)
            self.node = self.node.left

        return next_node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.node is not None or len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
