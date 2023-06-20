from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: prefix sum, array, 
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefix_sum = [0]
        tot = 0
        for num in nums:
            tot += num
            prefix_sum.append(tot)
            
        avgs = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i - k < 0 or i + k >= len(nums):
                continue

            count = 2*k + 1
            tot = prefix_sum[i+k+1]-prefix_sum[i-k]
            average = tot // count
            avgs[i] = average
            
        return avgs