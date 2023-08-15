from collections import defaultdict
from typing import Dict, List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def find(self, node: int, parent: Dict[int, int]) -> int:
        if parent[node] != node:
            parent[node] = self.find(parent[node], parent)
            
        return parent[node]
    
    
    
    def union(self, node1: int, node2: int, parent: Dict[int, int]) -> int:
        
        p1, p2 = parent[node1], parent[node2]
        
        if p1 < p2:
            parent[p2] = p1
        else:
            parent[p1] = p2
    
    
    # O(n) time,
    # O(n) space,
    # Approach: union find, graph, linked list, 
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        graph = defaultdict(set)
        prev = None
        curr = head
        
        while curr:
            if prev:
                graph[curr.val].add(prev.val)
            if curr.next:
                graph[curr.val].add(curr.next.val)
            prev = curr
            curr = curr.next
        
        parent = {}
        for num in nums:
            parent[num] = num

        for num in nums:
            for nbr in graph[num]:
                if nbr not in parent:
                    continue
                if self.find(num, parent) != self.find(nbr, parent):
                    self.union(num, nbr, parent)
        
        for num in nums:
            self.find(num, parent)
        
        return len(set(parent.values()))