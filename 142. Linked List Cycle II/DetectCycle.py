

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: two pointers, floyd warshall
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        slow = head
        fast = head
        
        while fast and fast.next:
            if slow is not None:
                slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
            
        if not fast or not fast.next:
            return None
            
        fast = head
        while fast != slow:
            if slow is not None:
                slow = slow.next
            if fast.next and fast.next.next != None:
                fast = fast.next
            
        return slow