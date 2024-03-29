from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    # O(n^2) time,
    # O(n) space,
    # Approach: stack, prefix sum, linked list, 
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(1001, head)
        stack = [dummy]
        prefix_sum = [0]
        
        curr = head
        while curr:
            [0, 1, 2, 0, ]
            prefix_sum.append(prefix_sum[-1]+curr.val)
            length = len(prefix_sum)
            for i in range(len(prefix_sum)-1):
                if prefix_sum[-1]-prefix_sum[i] == 0:
                    length = i+1
                    break
            stack.append(curr)
            while len(stack) > length:
                stack.pop()
                prefix_sum.pop()
                
            stack[-1].next = curr.next
            curr = curr.next
                
        return dummy.next
    
    
    # O(n) time,
    # O(n) space,
    # Approach: stack, prefix sum, hash map, linked list
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(1001, head)
        stack = [dummy]
        prefix_sum = [0]
        visited = {0: 1}
        
        curr = head
        while curr:
            prefix_sum.append(prefix_sum[-1]+curr.val)
            length = visited.get(prefix_sum[-1], len(prefix_sum))
            stack.append(curr)
            visited[prefix_sum[-1]] = len(prefix_sum)
            while len(stack) > length:
                stack.pop()
                if prefix_sum[-1] in visited:
                    visited.pop(prefix_sum[-1])
                prefix_sum.pop()
            visited[prefix_sum[-1]] = len(prefix_sum)  
            stack[-1].next = curr.next
            curr = curr.next
                
        return dummy.next