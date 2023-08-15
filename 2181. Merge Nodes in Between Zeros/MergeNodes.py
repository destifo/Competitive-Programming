from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: linked list, 
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        dummy = curr_new = ListNode()
        
        curr_tot = 0
        while curr:
            if curr.val == 0:
                new_node = ListNode(curr_tot)
                curr_tot = 0
                curr_new.next = new_node
                curr_new = curr_new.next
            else:
                curr_tot += curr.val
            curr = curr.next
            
        return dummy.next