from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: brainteaser, 
    def minOperations(self, boxes: str) -> List[int]:
        tot, cnt = 0, 0
        ans = [0 for _ in range(len(boxes))]
        
        for i in range(len(boxes)):
            tot += cnt
            ans[i] += tot
            if boxes[i] == '1':
                cnt += 1
        
        tot, cnt = 0, 0
        for i in range(len(boxes)-1, -1, -1):
            tot += cnt
            ans[i] += tot
            if boxes[i] == '1':
                cnt += 1
                
        return ans