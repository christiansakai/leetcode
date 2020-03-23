# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        while l1 is not None:
            stack1.append(l1.val)
            l1 = l1.next
            
        stack2 = []
        while l2 is not None:
            stack2.append(l2.val)
            l2 = l2.next
            
        stack = []
        carry = 0    
        while len(stack1) > 0 or len(stack2) > 0:
            if len(stack1) > 0 and len(stack2) > 0:
                val1 = stack1.pop()
                val2 = stack2.pop()
                
                total = carry + val1 + val2
                if total >= 10:
                    carry = 1
                    total = total - 10
                else:
                    carry = 0    
                    
                stack.append(total)
            elif len(stack1) > 0:
                val1 = stack1.pop()
                
                total = carry + val1    
                if total >= 10:
                    carry = 1
                    total = total - 10
                else:
                    carry = 0    
                    
                stack.append(total)
            else: 
                val2 = stack2.pop()
                
                total = carry + val2   
                if total >= 10:
                    carry = 1
                    total = total - 10
                else:
                    carry = 0    
                    
                stack.append(total)
                
        if carry == 1:
            stack.append(carry)
            
        head = None
        node = head
        while len(stack) > 0:
            val = stack.pop()
            
            if head is None:
                head = ListNode(val)
                node = head
            else:
                node.next = ListNode(val)    
                node = node.next
            
        return head
