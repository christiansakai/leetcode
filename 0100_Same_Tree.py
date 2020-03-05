# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # Iterative
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False

        p_queue = [p]
        q_queue = [q]

        while len(p_queue) > 0 and len(q_queue) > 0:
            p = p_queue.pop(0)
            q = q_queue.pop(0)

            not_same =\
                (p is not None and q is None) or\
                (p is None and q is not None) or\
                (p is not None and q is not None and p.val != q.val)

            if not_same:
                return False

            if p is not None:
                p_queue.append(p.left)
                p_queue.append(p.right)

            if q is not None:
                q_queue.append(q.left)
                q_queue.append(q.right)

        return len(p_queue) == 0 and len(q_queue) == 0
