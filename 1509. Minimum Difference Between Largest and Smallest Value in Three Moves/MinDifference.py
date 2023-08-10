from typing import List


class Solution:
    
    def findMinDiff(self, left: int, right: int, rem: int, nums: List[int]) -> int:
        
        if left == right:
            return 0
        
        if rem == 0:
            return nums[right]-nums[left]
        
        remove_left = self.findMinDiff(left+1, right, rem-1, nums)
        remove_right = self.findMinDiff(left, right-1, rem-1, nums)
        
        return min(remove_left, remove_right)
    
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: recursion, decison tree
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        return self.findMinDiff(0, len(nums)-1, 3, nums)
    
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: greedy, sorting, 
    def minDifference2(self, nums: List[int]) -> int:
        if len(nums) <= 4:  return 0
        
        nums.sort()
        moves = 3
        ans = nums[-1]-nums[moves]
        for i in range(moves):
            ans = min(ans, nums[-4+i]-nums[i])
            
        return ans