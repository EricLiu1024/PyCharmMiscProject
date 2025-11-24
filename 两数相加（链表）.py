class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        p1,p2 = l1,l2
        carry = 0
        while p1 or p2 or carry:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            sum = val1 + val2 + carry
            carry = sum // 10
            digit = sum % 10
            current.next= ListNode(digit)
            current = current.next
            if p1: p1 = p1.next
            if p2: p2 = p2.next
        return (dummy_head.next)
