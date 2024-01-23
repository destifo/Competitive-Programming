from collections import Counter
from typing import Dict, List


class Solution:
    
    def updateDict(sef, curr: Dict[str, int], change: Dict[str, int], operation: str) -> None:
        
        for k, v in change.items():
            if operation == 'add':
                curr[k] = curr.get(k, 0) + v
            else:
                curr[k] -= v
                if curr[k] == 0:
                    curr.pop(k)
                
    
    def conflict(self, curr: Dict[str, int], change: Dict[str, int]) -> bool:
        
        for ch, v in change.items():
            if ch in curr or v > 1:
                return True
            
        return False
    
    
    # O(2^len(arr)) time,
    # O(len(arr)) space,
    # Approach: backtracking, 
    def findMaxLength(self, i: int, count: List[Dict[str, int]], arr: List[str], curr: Dict[str, int]) -> int:
        
        if i == len(count):
            return 0
        
        take = float('-inf')
        if not self.conflict(curr, count[i]):
            self.updateDict(curr, count[i], 'add')
            take = len(arr[i]) + self.findMaxLength(i+1, count, arr, curr)
            self.updateDict(curr, count[i], 'remove')
            
        skip = self.findMaxLength(i+1, count, arr, curr)
        
        return max(take, skip)
    
    
    def maxLength(self, arr: List[str]) -> int:
        count = [Counter(string) for string in arr]
        
        return self.findMaxLength(0, count, arr, {})