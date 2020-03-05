# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        sub_prob = self.reverseList(head.next)
        if sub_prob is None:
            return head

        head.next = None

        temp = sub_prob
        while temp is not None and temp.next is not None:
            temp = temp.next

        temp.next = head
        return sub_prob
