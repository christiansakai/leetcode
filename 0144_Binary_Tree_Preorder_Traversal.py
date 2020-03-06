# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        
        self.recurse(root, result)
        return result
    
    def recurse(self, root: TreeNode, result: List[int]):
        if root is None:
            return

        result.append(root.val)
        self.recurse(root.left, result)
        self.recurse(root.right, result)
        
    # Iterative
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        result = []
        stack = [root]

        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return result



