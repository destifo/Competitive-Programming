from collections import deque
from typing import List


class Solution:
    
    def flipBit(self, number, position):
        mask = 1 << position
        flipped_number = number ^ mask
        return flipped_number
        
    def yFunction(self, x: int) -> int:
        return 3*x + 1
    
    def getNeighbors(self, state: int, n: int,) -> List[int]:
        nbrs = []
        
        curr_num = state
        for i in range(1, n):
            curr_num = self.flipBit(curr_num, i)
        nbrs.append(curr_num)
            
        curr_num = state
        for i in range(1, n, 2):
            curr_num = self.flipBit(curr_num, i)
        nbrs.append(curr_num)
            
        curr_num = state
        for i in range(0, n, 2):
            curr_num = self.flipBit(curr_num, i)
        nbrs.append(curr_num)
        
        i = 0
        while self.yFunction(i) < n:
            curr_num = self.flipBit(curr_num, self.yFunction(i))
            i += 1
        nbrs.append(curr_num)  
        
        return nbrs
            
            
    # O(n*press) time,
    # O(n*space) space,
    # Approach: bfs, bit manipulation, 
    def flipLights(self, n: int, presses: int) -> int:
        answer = set()
        queue = deque()
        queue.append(2**n - 1)
        answer.add(queue[0])
        
        while presses and queue:
            presses -= 1
            queue_len = len(queue)
            answer = set()
            for _ in range(queue_len):
                state = queue.popleft()
                nbrs = self.getNeighbors(state, n)
                for nbr in nbrs:
                    if nbr in answer:
                        continue
                    answer.add(nbr)
                    queue.append(nbr)

        return len(answer)