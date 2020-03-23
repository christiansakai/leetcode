"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self.recurse(head)
        return head
        

    def recurse(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        child = self.recurse(root.child)
        next = self.recurse(root.next)
        
        if child is not None and next is not None:
            root.child = None
            root.next = child
            child.prev = root
            
            temp_child = child
            while temp_child is not None and temp_child.next is not None:
                temp_child = temp_child.next

            temp_child.next = next
            next.prev = temp_child
        elif child is not None:
            root.child = None
            root.next = child    
            child.prev = root
        elif next is not None:
            root.child = None
            root.next = next    
            next.prev = root
            
        return root
            
