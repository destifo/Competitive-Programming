'''
https://leetcode.com/problems/linked-list-cycle/
'''


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # O(n) time,
    # O(n) space, 
    # Approach: hashmap,
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vstd  = set()
        
        curr = head
        
        while curr:
            if curr in vstd:
                return True
            vstd.add(curr)
            curr = curr.next
            
        return False