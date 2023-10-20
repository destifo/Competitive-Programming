from typing import List


class Solution:
    
    # O(n^2) time,
    # O(1) space,
    # Approach: bit, 
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        
        for i in range(len(arr)-1):
            tot = arr[i]
            for j in range(i+1, len(arr)):
                tot ^= arr[j]
                if tot == 0:
                    ans += (j-i)
        
        return ans