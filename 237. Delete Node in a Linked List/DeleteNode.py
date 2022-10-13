# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: linked list, 
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = None
        curr = node
        nxt = node.next
        
        while nxt:
            curr.val = nxt.val
            prev = curr
            curr = nxt
            nxt = nxt.next
        
        prev.next = None

    
    # O(1) time,
    # O(1) space,
    # Approach: linked list
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next