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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        if not head.next:
            return head
        
        # find the mid node
        slow, fast = head, head
        
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        mid_node = slow
        
        # break list into two
        prev.next = None
        
        # reverse second half
        prev, curr = mid_node, mid_node.next
        prev.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # reorder the list
        dummy = ListNode(0)
        curr_last = dummy
        curr1, curr2 = head, prev
        
        while curr1 and curr2:
            nxt1, nxt2 = curr1.next, curr2.next
            curr1.next, curr2.next = curr2, None
            curr_last.next = curr1
            curr_last = curr2
            curr1, curr2 = nxt1, nxt2
            
        if curr2:
            curr_last.next = curr2
            
        return dummy.next