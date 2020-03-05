# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        if head.next is None:
            return head

        sub_prob = self.swapPairs(head.next.next)
        
        temp_head = head
        head = head.next
        head.next = temp_head 
        head.next.next = sub_prob 
        
        return head
