from typing import Dict, List


class Solution:
    
    def areConscInc(self, index: int, nums: List[int]) -> bool:
        
        return nums[index+1]-nums[index] == 1 and nums[index+2]-nums[index+1] == 1
    
    
    def areNextThreeEq(self, index: int, nums: List[int]) -> bool:   
        return nums[index] == nums[index+1] == nums[index+2]
    
    
    def canBePartitioned(self, index: int, nums: List[int], memo: Dict[int, bool]) -> bool:
        
        if index == len(nums):
            return True
        
        if index == len(nums)-1:
            return False
        
        if index in memo:
            return memo[index]
        
        if nums[index] == nums[index+1]:
            if self.canBePartitioned(index+2, nums, memo):
                return True
            
        if index+2 < len(nums) and (self.areNextThreeEq(index, nums) or self.areConscInc(index, nums)):
            if self.canBePartitioned(index+3, nums, memo):
                return True
        
        memo[index] = False
        return False
    
    
    # O(n) time,
    # O(n) space,
    # Approach: top down dp,
    # Why dp: here dp lets us know a sub problem where the answer is false, so we wouldn't waste time analyzing that sub problem again(which evaluates to false), but in case we get a "True" value, we simply return, so the memo only stores the value for sub problems where they aren't valid partitions, 
    def validPartition(self, nums: List[int]) -> bool:
        return self.canBePartitioned(0, nums, {})
    
    
    # O(n) time,
    # O(n) space,
    # Approach: bottom up dp,
    def validPartition2(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums)+1)]
        dp[len(nums)] = True
        
        for index in range(len(nums)-2, -1, -1):
            if nums[index] == nums[index+1]:
                dp[index] = dp[index+2]
            if dp[index]:   continue
            if index+2 < len(nums) and (self.areNextThreeEq(index, nums) or self.areConscInc(index, nums)):
                dp[index] = dp[index+3]
        
        return dp[0]