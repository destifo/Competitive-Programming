from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    
    def getSize(self, head: Optional[ListNode]) -> int:  
        size = 0
        curr = head
        
        while curr:
            size += 1
            curr = curr.next
            
        return size
    

    # O(n) time, specifically 2 passes, 2n
    # O(1) space,
    # Approach: couting, linked list
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        size = self.getSize(head)
        first_pos, second_pos = k, (size-k) + 1
        first_node, second_node = None, None
        
        curr = head
        for i in range(1, size+1):
            if i == first_pos:
                first_node = curr
            if i == second_pos:
                second_node = curr
                
            curr = curr.next
            
        first_node.val, second_node.val = second_node.val, first_node.val
            
        return head
    

    # O(n) time, one pass
    # O(1) space,
    # Apporoach: two pointers, 
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        left, right = head, head
        for _ in range(k-1):
            right = right.next
            
        first_node = right
        while right.next:
            left = left.next
            right = right.next
        second_node = left
            
        second_node.val, first_node.val = first_node.val, second_node.val
        return head