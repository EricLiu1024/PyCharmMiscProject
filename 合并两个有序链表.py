# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first_1 = list1
        first_2 = list2
        if first_1.val > first_2.val:
            first_1.val, first_2.val = first_1.val, first_2.val
        current1 = list1
        current2 = list2
        while current1:
            if current2.val < current1.next.val:
                chang_node = current2
                current1.next = current2
                chang_node.next = current1.next
            current = current.next
