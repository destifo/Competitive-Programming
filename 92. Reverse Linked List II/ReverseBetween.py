from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    # O(n) time, one pass
    # O(1) space,
    # Approach: two pointers, linked list 
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = dummy = ListNode(0, head)
        curr = head
        
        while left > 1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1
            
        reverse_start = prev
        reversed_tail = curr
        while right > 0:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            right -= 1
            
        reverse_start.next = prev
        reversed_tail.next = curr
        
        return dummy.next