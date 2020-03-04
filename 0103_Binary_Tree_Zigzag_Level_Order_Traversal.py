# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []

        if root is None:
            return result

        queue = [root]

        while len(queue) > 0:
            queue_len = len(queue)
            level = []

            for i in range(0, queue_len):
                node = queue.pop(0)

                if len(result) % 2 == 0:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            result.append(level)

        return result
