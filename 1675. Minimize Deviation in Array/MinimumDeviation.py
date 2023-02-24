from typing import List


class Solution:
    
    # O(nlog(max(nums)) + ) time,
    # O(1) space,
    # Approach: heap, greedy
    def minimumDeviation(self, nums: List[int]) -> int:
        
        '''
        
        
        '''
        max_val = 0
        min_val = float('inf')
        for i, num in enumerate(nums):
            while num % 2 == 0:
                num //=2
                
            nums[i] = (num, nums[i])
            min_val = min(min_val, num)
            max_val = max(max_val, num)
            
        
        heapq.heapify(nums)
        ans = max_val - min_val
        while nums[0][0] % 2 == 1 or nums[0][0] < nums[0][1]:
            curr_min, curr_limit = heapq.heappop(nums)
            max_val = max(max_val, curr_min*2)
            heapq.heappush(nums, (curr_min*2, curr_limit))
            ans = min(ans, max_val-nums[0][0])
            
        return ans