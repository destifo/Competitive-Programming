'''

'''


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: Two pointer,
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
            
        curr = head
        while prev:
            if curr.val != prev.val:
                return False
            curr = curr.next
            prev = prev.next
        
        return True