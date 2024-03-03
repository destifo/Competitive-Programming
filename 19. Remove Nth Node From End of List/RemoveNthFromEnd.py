from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    # O(n) time, one pass
    # O(1) space,
    # Approach: two pointers, 
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first, second = dummy, dummy
        
        while n > 0:
            first = first.next
            n -= 1
        
        while first.next:
            first = first.next
            second = second.next
            
        prev = second.next
        second.next = prev.next
        prev.next = None
        
        return dummy.next
            
        