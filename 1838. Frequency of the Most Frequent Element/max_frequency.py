'''
https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/
'''

class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        nums.sort()
        left_end, right_end = 0, 0
        total, max_freq = 0, 0

        while right_end < len(nums):
            total += nums[right_end]

            while (right_end - left_end + 1)*nums[right_end] > total + k:
                total -= nums[left_end]
                left_end += 1

            max_freq = max(max_freq, (right_end - left_end + 1))
            right_end += 1

        return max_freq

sol = Solution()
print(sol.maxFrequency([3,9,6], 2))