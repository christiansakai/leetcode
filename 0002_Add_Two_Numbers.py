# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2

        if l2 is None:
            return l1
        
        carry = 0
        head_val = l1.val + l2.val
        if head_val >= 10:
            carry = 1
            head_val = head_val - 10
            
        head = ListNode(head_val)
        node = head
        l1 = l1.next
        l2 = l2.next

        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                val = carry + l1.val + l2.val
                if val >= 10:
                    carry = 1
                    val = val - 10
                else:
                    carry = 0
                    
                node.next = ListNode(val)
                node = node.next
                
                l1 = l1.next
                l2 = l2.next
            elif l1 is not None:
                val = carry + l1.val

                if val >= 10:
                    carry = 1
                    val = val - 10
                else:
                    carry = 0
                    
                node.next = ListNode(val)
                node = node.next
                
                l1 = l1.next
            else:
                val = carry + l2.val

                if val >= 10:
                    carry = 1
                    val = val - 10
                else:
                    carry = 0
                    
                node.next = ListNode(val)
                node = node.next
                
                l2 = l2.next
                
        if carry == 1:
            node.next = ListNode(carry)
                
        return head
