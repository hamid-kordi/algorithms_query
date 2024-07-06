"""

You are given two non-empty linked lists 
representing two non-negative integers. 
The digits are stored in reverse order, 
and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any 
leading zero, except the number 0 itself

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        curr, p1, p2 = head, l1, l2
        carry = 0
        while p1 or p2 or carry:
            p1, value1 = (p1.next, p1.val) if p1 else (p1, 0)
            p2, value2 = (p2.next, p2.val) if p2 else (p2, 0)
            suumm = value1 + value2 + carry
            carry, result = divmod(suumm, 10)
            curr.next = ListNode(result)
            curr = curr.next
            return head.next
