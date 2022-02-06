"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        count = [0] * len(nums)
        for i in range(len(nums)):
            j = 0
            while (j < len(nums)):
                if (nums[i] > nums[j]):
                    count[i] += 1
                j +=1
        return count

sol = Solution()
print(sol.smallerNumbersThanCurrent([7,7,7,7]))        
