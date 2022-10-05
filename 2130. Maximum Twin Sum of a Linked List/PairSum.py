from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # O(n) time, 
    # O(1) space,
    # Approach: two pointers, 
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        
        # find the mid
        while fast:
            fast = fast.next.next
            slow = slow.next
            
        nxt = None
        curr = slow.next
        prev = slow
        prev.next = None
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        max_twin_sum = float('-inf')
        curr = head
        while prev:
            curr_twin_sum = prev.val + curr.val
            max_twin_sum = max(max_twin_sum, curr_twin_sum)
            prev = prev.next
            curr = curr.next
            
        return max_twin_sum