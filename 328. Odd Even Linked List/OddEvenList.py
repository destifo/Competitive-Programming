

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: linked list
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = ListNode(0)
        even_head = ListNode(0)
        
        curr_odd = odd_head
        curr_even = even_head
        index = 1
        curr = head
        
        while curr:
            nxt = curr.next
            curr.next = None
            if index % 2 == 0:
                curr_even.next = curr
                curr_even = curr_even.next
            else:
                curr_odd.next = curr
                curr_odd = curr_odd.next
            curr = nxt
            index += 1
            
        
        curr_odd.next = even_head.next
        
        return odd_head.next