from collections import defaultdict
from typing import List, Set


class Solution:
    
    def findConsc(self, num: int, nums: Set[int], streak: List[int]) -> None:
        if streak[num] != 0:
            return streak[num]
        
        nxt = num + 1
        consc_length = 1
        if nxt in nums:
            self.findConsc(nxt, nums, streak)
            consc_length += streak[nxt]
            
        streak[num] = consc_length
    
    
    # O(n) time,
    # O(n) space,
    # Approach: memoization, hash table
    def longestConsecutive(self, nums: List[int]) -> int:
        streak = defaultdict(int)
        nums_set = set(nums)
        ans = 0
        
        for num in nums:
            self.findConsc(num, nums_set, streak)
            ans = max(ans, streak[num])
            
        return ans