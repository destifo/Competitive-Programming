from typing import List


class Solution:
    
    def burstLast(self, left, right, nums, memo):
        
        if left > right:
            return 0
        
        if (left, right) in memo:
            return memo[(left, right)]
        
        max_coins = 0
        for i in range(left, right+1):
            curr_coins = nums[left-1] * nums[i] * nums[right+1] + self.burstLast(left, i-1, nums, memo) + self.burstLast(i+1, right, nums, memo)
            max_coins = max(max_coins, curr_coins)
        
        memo[(left, right)] = max_coins
        return max_coins
    
    
    # O(n^3) time,
    # O(n^2) space,
    # Approach: top down dp, 
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        return self.burstLast(1, len(nums)-2, nums, {})