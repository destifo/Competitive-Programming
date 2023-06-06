from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    
    def copyNode(self, node, copied_pair):
        copy = Node(node.val)
        copied_pair[node] = copy

        if node.random and node.random not in copied_pair:
            copied_pair[node.random] = self.copyNode(node.random, copied_pair)
            
        copy.random = copied_pair[node.random] if node.random in copied_pair else None
        
        return copy
    
    
    # O(n) time,
    # O(n) space,
    # Approach: recursion, hashtable, 
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied_pair = {}
        if not head:
            return head
        
        copied_head = self.copyNode(head, copied_pair)
        copied_pair[head] = copied_head
        
        curr = head
        curr_copy = copied_head
        
        curr = curr.next
        while curr:
            if curr not in copied_pair:
                self.copyNode(curr, copied_pair)
            
            copied_node = copied_pair[curr]
            curr_copy.next = copied_node
            curr_copy = copied_node
            curr = curr.next
        
        return copied_head