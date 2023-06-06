'''
https://leetcode.com/problems/4sum/
'''


class Solution:
    # O(n^3) time,
    # O(len(ans)) space,
    # Approach: Two Pointers
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        
        for i, num1 in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:  continue
            for j in range(i+1, n):
                num2 = nums[j]
                if j > i+1 and nums[j] == nums[j-1]:  continue
                l, r = j+1, n-1
                while l < r:
                    four_sum = num1 + num2 + nums[l] + nums[r]
                    if four_sum > target:
                        r -=1
                    elif four_sum < target:
                        l +=1
                    else:
                        ans.append([num1, num2, nums[l], nums[r]])
                        r -=1
                        while r > l and nums[r] == nums[r+1]:
                            r -=1
        
        return ans