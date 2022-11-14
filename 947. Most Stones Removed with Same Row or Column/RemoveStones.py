from collections import defaultdict
from typing import List, Set, Tuple, Dict


class Solution:
    
    def countConnected(self, coord: List[int], visited: Set[Tuple[int, int]], rows, cols):
        
        row, col = coord
        if (row, col) in visited:
            return 0
        
        visited.add((row, col))
        count = 1
        
        for stone in rows[row]:
            count += self.countConnected(stone, visited, rows, cols)
            
        for stone in cols[col]:
            count += self.countConnected(stone, visited, rows, cols)
        
        return count
    
    
    # O(V + E) time,
    # O(V + E) space,
    # Approach: dfs, graph
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        for stone in stones:
            rows[stone[0]].append(stone)
            cols[stone[1]].append(stone)
            
        visited = set()
        answer = 0
        for stone in stones:
            answer += max(0, self.countConnected(stone, visited, rows, cols)-1)
        
        return answer