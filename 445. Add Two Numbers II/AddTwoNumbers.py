from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def findLength(self, node: ListNode) -> int:
        length = 0
        
        while node:
            length += 1
            node = node.next
            
        return length
    
    
    # O(n) time,
    # O(n) space,
    # Approach: Linked list, 
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        len1, len2 = self.findLength(l1), self.findLength(l2)
        
        temp = []
        while len1 > 0 and len2 > 0:
            if len1 == len2:
                temp.append(l1.val+l2.val)
                l1, l2 = l1.next, l2.next
                len1 -= 1
                len2 -=1
            elif len1 > len2:
                temp.append(l1.val)
                l1 = l1.next
                len1 -= 1
            else:
                temp.append(l2.val)
                l2 = l2.next
                len2 -= 1
            
        for i in range(len(temp)-1, 0, -1):
            val = temp[i]
            if val >= 10:
                temp[i-1] += 1
                temp[i] %= 10
        
        ans = ListNode(temp[0])
        curr = ans
        if temp[0] >= 10:
            ans = ListNode(1)
            new_node = ListNode(temp[0]%10)
            ans.next = new_node
            curr = new_node
            
        for i in range(1, len(temp)):
            new_node = ListNode(temp[i])
            curr.next = new_node
            curr = curr.next
            
        return ans