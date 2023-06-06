

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def size(self, head: Optional[ListNode]) -> int:
        
        nodes = 0
        
        while head:
            nodes += 1
            head = head.next
            
        return nodes
    
    
    # O(n) time,
    # O(k) space,
    # Approach: iteration, math
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        size = self.size(head)
        
        partition_size = size // k
        rem = size % k
        if partition_size == 0:
            partition_size = 1
            rem = 0
        
        curr = head
        partitions = []
        curr_head = head
        count = 0
        
        while curr:
            
            count += 1
            if count == partition_size:
                if rem:
                    curr = curr.next
                    rem -= 1

                partitions.append(curr_head)
                if curr:
                    curr_head = curr.next
                    curr.next = None
                curr = curr_head
                count = 0
                
            else:
                curr = curr.next
                
        while len(partitions) < k:
            partitions.append(None)
            
        return partitions