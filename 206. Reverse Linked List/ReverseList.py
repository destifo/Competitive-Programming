from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # O(n) time,
    # O(1) space,
    # Approach: linked list, two pointers
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev, curr = head, head.next
        prev.next = None
        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt

        return prev
