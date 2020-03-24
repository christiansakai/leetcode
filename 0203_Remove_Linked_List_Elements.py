# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        
        while head and head.val == val:
            head = head.next
            
        prev = None
        node = head
        while node is not None:
            if node.val == val:
                prev.next = node.next
                node = node.next
            else:
                prev = node
                node = node.next
            
        return head
            
