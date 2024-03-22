'''
https://leetcode.com/problems/palindrome-linked-list/
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
        
        while fast is not None and fast.next is not None:
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
    
    
    # O(n) time,
    # O(1) space,
    # Approach: linked list, two pointers, hair-tortoise
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        slow, fast = head, head
        
        # find middle node
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # reverse nodes starting from middle
        prev.next = None
        prev, curr = slow, slow.next
        prev.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # check pali
        left, right = head, prev
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True