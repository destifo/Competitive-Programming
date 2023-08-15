from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: linked list, two pointers, 
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = curr1 = ListNode()
        dummy2 = curr2 = ListNode()
        curr = head

        while curr:
            if curr.val < x:
                curr1.next = curr
                curr1 = curr1.next
                curr = curr.next
                curr1.next = None
            else:
                curr2.next = curr
                curr2 = curr2.next
                curr = curr.next
                curr2.next = None
        
        curr1.next = dummy2.next
        return dummy1.next