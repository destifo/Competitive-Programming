import heapq
from typing import List


class Solution:
    
    def countSol(self, row: List[int]) -> int:
        
        index = -1
        lo, hi = 0, len(row)-1
        
        while lo <= hi:
            mid = (lo+hi)//2
            if row[mid] == 1:
                index = mid
                lo = mid+1
            else:
                hi = mid-1
                
        return index+1
    
    
    # O(n*logm*logn) time,
    # O(1) space,
    # Approach: heap, binary search, 
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        rows, cols = len(mat), len(mat[0])
        heap = []
        
        for i, row in enumerate(mat):
            count = self.countSol(row)
            if len(heap) < k:
                heapq.heappush(heap, (-count, -i))
            else:
                if -heap[0][0] > count or (-heap[0][0] == count and -heap[0][1] > i):
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-count, -i))
                    
        ans = []
        while heap:
            ans.append(-heapq.heappop(heap)[1])
            
        return ans[::-1]