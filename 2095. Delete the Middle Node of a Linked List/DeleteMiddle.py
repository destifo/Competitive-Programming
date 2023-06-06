from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # O(n) time, n//2 time actually
    # O(1) space,
    # Approach: two pointers, linked list
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if slow == head:
            head = None
        elif not slow.next:
            head.next = None
        elif slow.next.next:
            slow.val = slow.next.val
            slow.next = slow.next.next
        else:
            slow.val = slow.next.val
            slow.next = None
            
        return head