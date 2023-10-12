from typing import List, Set, Tuple


class Solution:
    
    def inBounds(self, row: int, col: int, heights: List[List[int]]) -> bool:

        if row < 0 or row >= len(heights):
            return False
        
        if col < 0 or col >= len(heights[0]):
            return False
        
        return True
    
    
    def getNeighbors(self, row: int, col: int, cost: int, heights: List[List[int]], visited: Set[Tuple[int]]) -> List[Tuple[int]]:
        
        nbrs = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        curr_height = heights[row][col]
        for x, y in directions:
            new_row, new_col = row+x, col+y
            if self.inBounds(new_row, new_col, heights) and abs(curr_height-heights[new_row][new_col]) <= cost and (new_row, new_col) not in visited:
                nbrs.append((new_row, new_col))
                
        return nbrs
    
    
    
    def isTherePath(self, row: int, col: int, cost: int, heights: List[List[int]], visited: Set[Tuple[int]]) -> bool:
        
        if row == len(heights)-1 and col == len(heights[0])-1:
            return True
        
        for nbr_row, nbr_col in self.getNeighbors(row, col, cost, heights, visited):
            visited.add((nbr_row, nbr_col))
            if self.isTherePath(nbr_row, nbr_col, cost, heights, visited):
                return True
            # visited.remove((nbr_row, nbr_col))
            
        return False
    
    
    # O(n*mlogh) time,
    # O(n*m) space,
    # Approach: binary search, depth first search
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        lo, hi = 0, (10**6)
        ans = hi
        
        while lo <= hi:
            mid = (lo+hi)//2
            if self.isTherePath(0, 0, mid, heights, {(0, 0)}):
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
                
        return ans