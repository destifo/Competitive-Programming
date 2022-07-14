'''
https://leetcode.com/problems/max-consecutive-ones/
'''


class Solution:
    # O(n) time, 
    # O(1) space,
    # approach: two pointer, sliding window
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        max_len = 0
        
        while r < n:
            if nums[l] == nums[r] and nums[r] == 1:
                max_len = max(max_len, r-l+1)
                r +=1
            elif l == r and nums[r] == 0:
                l +=1
                r +=1
            else:
                l = r
                r +=1
                
        return max_len