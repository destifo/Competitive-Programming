'''
https://leetcode.com/problems/frequency-of-the-most-frequent-element/submissions/
'''

from typing import List


class Solution:
    # O(nlogn) time,
    # O(1) space,
    # Approach: two pointers, sorting
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

    
    # O(nlogn) time,
    # O(n) space,
    # Approach: two pointers, sorting, prefix sum
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        
        prefix_sum = [0]
        tot = 0
        for i in range(n):
            tot += nums[i]
            prefix_sum.append(tot)
            
        l, r = 0, 0
        ans = 0
        
        while r < n:
            
            while (r-l+1) * nums[r] > prefix_sum[r+1] - prefix_sum[l]+k:
                l +=1
                
            ans = max(ans, r-l+1)
            r +=1
            
        return ans

sol = Solution()
print(sol.maxFrequency([3,9,6], 2))