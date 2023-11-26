from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: array, 
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        curr_max = -1
        ans = [-1 for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            ans[i] = curr_max
            curr_max = max(curr_max, arr[i])
            
        return ans