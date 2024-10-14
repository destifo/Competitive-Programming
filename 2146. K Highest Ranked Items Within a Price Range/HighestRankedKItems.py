from collections import deque
import heapq
from typing import List


class Solution:
    
    def inBound(self, row: int, col: int, grid: List[List[int]]) -> bool:
        
        if row < 0 or row >= len(grid):
            return False
        
        if col < 0 or col >= len(grid[0]):
            return False
        
        return True
    
    
    def getNeighbors(self, row: int, col: int, grid: List[List[int]]) -> List[List[int]]:
        nbrs = []
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for x, y in directions:
            new_row, new_col = row+x, col+y
            if self.inBound(new_row, new_col, grid) and grid[new_row][new_col] != 0:
                # print(grid)
                # print(grid[new_row][new_col])
                nbrs.append([new_row, new_col])
        # print(nbrs)
        return nbrs
    
    
    def getInRangeItems(self, pricing: List[int], start: List[int], grid: List[List[int]], ans: List[List[int]]) -> None:
        
        dist = 0
        queue = deque()
        queue.append((start[0], start[1]))
        
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                row, col = queue.popleft()
                curr_val = abs(grid[row][col])
                low, high = pricing
                if curr_val >= low and curr_val <= high:
                    heapq.heappush(ans, (dist, curr_val, row, col))
                
                grid[row][col] = 0
                for nbr_row, nbr_col in self.getNeighbors(row, col, grid):
                    if grid[nbr_row][nbr_col] <= 0:
                        continue
                    queue.append((nbr_row, nbr_col))
                    grid[nbr_row][nbr_col] *= -1
            dist += 1
        
        return ans
    
    
    # O(n*mlogm*n) time,
    # O(n*m) space,
    # Approach: heap, bfs
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        items = []
        self.getInRangeItems(pricing, start, grid, items)

        kRanked = []
        while k > 0 and items:
            item = heapq.heappop(items)
            k -= 1
            kRanked.append([item[-2], item[-1]])
            
        return kRanked