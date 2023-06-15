from collections import deque
import heapq
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # O(klogk + n) time,
    # O(k + n) space,
    # Approach: heap, bfs, tree, 
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        heap = []
        queue = deque()
        queue.append(root)
        
        while queue:
            queue_len = len(queue)
            level_sum = 0
            for _ in range(queue_len):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            if len(heap) < k:
                heapq.heappush(heap, level_sum)
            elif level_sum > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, level_sum)
                
        return -1 if len(heap) < k else heap[0]