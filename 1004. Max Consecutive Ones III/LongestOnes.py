'''
https://leetcode.com/problems/max-consecutive-ones-iii/submissions/
'''

class Solution:
    def longestOnes(self, nums, k: int):
        n = len(nums)
        l = 0
        r = 0
        max_len = 0
        
        while r < n:
            if nums[r] == 0:
                k -=1

            if k < 0:
                if nums[l] == 0:
                    k +=1
                l +=1
            r +=1
            
        max_len = r - l    
        return max_len
            
sol = Solution()
print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))