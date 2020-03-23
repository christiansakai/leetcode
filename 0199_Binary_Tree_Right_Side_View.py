# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        result = []
        queue = [root]
        
        while len(queue) > 0:
            qlen = len(queue)
            for i in range(0, qlen):
                node = queue.pop(0)
                
                if i == qlen - 1:
                    result.append(node.val)
                    
                if node.left is not None:
                    queue.append(node.left)
                    
                if node.right is not None:
                    queue.append(node.right)
                    
        return result
        
