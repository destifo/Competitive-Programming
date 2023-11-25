from typing import List


class Solution:
    
    # O(n) time, two passes
    # O(1) space,
    # Approach: counting, math, prefix sum
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        '''
        
        [2, 3, 5]
        
        prev = 2
        
        going left to right: ans = 1 => (prev_ab + i*abs(nums[i]-nums[i-1]))
        
        going right to left: ans = 2 => prev_ab + (n-i-1)*abs(nums[i+1]-nums[i])
        
        '''
        n = len(nums)        
        ans = [0 for _ in range(n)]
        
        curr_abs = 0
        for i in range(1, n):
            curr_abs += i*abs(nums[i]-nums[i-1])
            ans[i] = curr_abs
            
        curr_abs = 0
        for i in range(n-2, -1, -1):
            curr_abs += (n-i-1)*abs(nums[i]-nums[i+1])
            ans[i] += curr_abs
            
        return ans