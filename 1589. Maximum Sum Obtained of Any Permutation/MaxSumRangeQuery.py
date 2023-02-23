from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: prefix sum, sorting, greedy
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        overlap = [0 for _ in range(len(nums))]
        for req in requests:
            start, end = req
            overlap[start] += 1
            if end+1 < len(nums):
                overlap[end+1] -=1
                
        prefix_sum = []
        tot = 0
        for i in range(len(overlap)):
            tot += overlap[i]
            prefix_sum.append(tot)
            
        nums.sort()
        prefix_sum.sort()
        
        MOD = (10**9) + 7
        max_sum = 0
        while nums:
            max_sum += (prefix_sum.pop() * nums.pop())
            
        return max_sum % MOD