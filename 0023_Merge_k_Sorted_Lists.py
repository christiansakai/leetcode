# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = None
        temp = None

        while True:
            smallest_index = self.get_smallest_index(lists)
            if smallest_index == -1:
                break

            if head is None:
                head = lists[smallest_index]
                temp = lists[smallest_index]
            else:
                temp.next = lists[smallest_index]
                temp = temp.next

            lists[smallest_index] = lists[smallest_index].next

        return head

    def get_smallest_index(self, lists: List[ListNode]) -> int:
        index = -1
        smallest = sys.maxsize

        for i in range(0, len(lists)):
            if lists[i] is not None and lists[i].val < smallest:
                index = i
                smallest = lists[i].val

        return index
