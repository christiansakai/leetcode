from typing import Tuple

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or head.next is None:
            return head
        
        pre_m, node_m = self.get_at_m(head, m)
        node_n, post_n = self.reverse(node_m, n - m)
        
        if pre_m is None:
            node_m.next = post_n
            return node_n
        
        pre_m.next = node_n
        node_m.next = post_n
        
        return head
    
    
    def get_at_m(self, head: ListNode, m) -> (ListNode, ListNode):
        prev = None
        node = head
        
        for i in range(0, m - 1):
            prev = node
            node = node.next
            
        return (prev, node)
    

    def reverse(self, node: ListNode, steps) -> (ListNode, ListNode):
        prev = None
        
        for i in range(steps + 1):
            next_temp = node.next
            node_temp = node
            
            node.next = prev
            
            node = next_temp
            prev = node_temp
            
        return (prev, node) 
