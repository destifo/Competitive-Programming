

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def insert(self, lo, hi, nums) -> Optional[TreeNode]:
        if lo > hi:
            return
        
        mid = (lo+hi)//2
        val = nums[mid]
        curr_node = TreeNode(val)
        curr_node.left = self.insert(lo, mid-1, nums)
        curr_node.right = self.insert(mid+1, hi, nums)
        
        return curr_node
    
    
    # O(n) time,
    # O(n) space,
    # Approach: binary search, 
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
            
        head = self.insert(0, len(nums)-1, nums)
        return head
    

    def getMiddle(self, node, end):
        slow = node
        fast = node
        
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    
    def insert(self, node, end) -> Optional[TreeNode]:
        if node == end:
            return
        
        mid = self.getMiddle(node, end)
        curr_node = TreeNode(mid.val)
        curr_node.left = self.insert(node, mid)
        curr_node.right = self.insert(mid.next, end)
        
        return curr_node
    
    
    # O(nlogn) time,
    # O(logn) space,
    # Approach: two pointers, linked list, recursion
    def sortedListToBST2(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        head = self.insert(head, None)
        return head