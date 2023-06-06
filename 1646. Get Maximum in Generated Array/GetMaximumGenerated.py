'''
https://leetcode.com/problems/get-maximum-in-generated-array/
'''


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: dp, tabulation
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        
        nums = [0 for i in range(n+1)]
        nums[0] = 0
        nums[1] = 1
        
        max_val = 1
        
        for i in range(2, n+1):
            if i % 2 == 0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2] + nums[(i//2) + 1]
                
            max_val = max(max_val, nums[i])
            
        return max_val