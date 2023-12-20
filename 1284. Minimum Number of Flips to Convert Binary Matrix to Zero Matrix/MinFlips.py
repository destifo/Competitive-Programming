from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple


class Solution:
    
    def getFlattnedIndex(self, row: int, col: int, cols: int) -> int:
        return row*cols + col
    
    
    def getNeighbors(self, row: int, col: int, mat: List[List[int]]) -> List[Tuple[int]]:
        
        nbrs = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for x, y in directions:
            new_row, new_col = row+x, col+y
            if 0 <= new_row < len(mat) and 0 <= new_col < len(mat[0]):
                nbrs.append((new_row, new_col))
                
        return nbrs
    
    
    def flip(self, index: int, prev_bits: List[int], nbrs: Dict[int, int]) -> None:
        bits = prev_bits[::]
        bits[index] += 1
        bits[index] %= 2
        
        for i in nbrs[index]:
            bits[i] += 1
            bits[i] %= 2
            
        return bits
    
    
    def getMinFlips(self, bits: List[int], nbrs: Dict[int, int], visited: Set[int]) -> int:
        
        min_flips = 0
        queue = deque()
        visited = set()
        queue.append(bits)
        
        while queue:
            queue_len = len(queue)
            for _ in range(queue_len):
                curr = queue.popleft()
                num = int("".join([str(d) for d in curr]), 2)
                if num == 0:
                    return min_flips
                
                if num in visited:
                    continue
                visited.add(num)
                
                for i in range(len(curr)):
                    nbr = self.flip(i, curr, nbrs)
                    queue.append(nbr)
                    
            min_flips += 1
        
        return -1
                
    
    # O(2^(m+n)) time, m -> rows, n -> cols
    # O(2^(m+n)) space,
    # Approach: bit masking, bfs, 
    def minFlips(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        bits = []
        nbrs = defaultdict(list)
        
        for row in range(ROWS):
            for col in range(COLS):
                bits.append(mat[row][col])
                
                index = self.getFlattnedIndex(row, col, COLS)
                for nbr_row, nbr_col in self.getNeighbors(row, col, mat):
                    nbrs[index].append(self.getFlattnedIndex(nbr_row, nbr_col, COLS))
                    
        return self.getMinFlips(bits, nbrs, set())