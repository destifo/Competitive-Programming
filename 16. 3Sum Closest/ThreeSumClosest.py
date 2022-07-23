'''
https://leetcode.com/problems/3sum-closest/
'''


class Solution:
    # O(n^2) time,
    # O(1) space,
    # Approach: Sorting, Two Pointers
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        diff = float('inf')
        nums.sort()
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:  continue
            l, r = i+1, n-1
            
            while l < r:
                three_sum = nums[l] + nums[r] + num
                if three_sum == target:
                    return target
                
                if abs(three_sum - target) < abs(diff):
                    diff = three_sum - target
                
                if three_sum < target:
                    l +=1
                else:
                    r -=1
                    
        return target + diff