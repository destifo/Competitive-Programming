from collections import defaultdict
from typing import List


class Solution:
    
    # O(n) time,
    # O(n + k) space,
    # Approach: hashtable, couting,
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0 for _ in range(k)]
        
        logger = defaultdict(set)
        for userId, time in logs:
            logger[userId].add(time)
            
        for actions in logger.values():
            answer[len(actions)-1] += 1
        
        return answer