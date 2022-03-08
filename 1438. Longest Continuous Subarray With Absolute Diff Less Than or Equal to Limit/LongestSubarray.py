"""
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/submissions/
"""

import collections


class Solution:
    def longestSubarray2(self, nums, limit: int):
        minQ = collections.deque([])
        maxQ = collections.deque([])
        longest = 0

        left = 0
        n = len(nums)
        for right in range(n):
            while minQ and minQ[-1] > nums[right]:
                minQ.pop()
            minQ.append(nums[right])

            while maxQ and maxQ[-1] < nums[right]:
                maxQ.append(nums[right])
            maxQ.append(nums[right])

            if (maxQ[0] - minQ[0] <= limit):
                longest = max(longest, right - left + 1)
            else:
                if maxQ[0] == nums[left]:
                    maxQ.popleft()
                if minQ[0] == nums[left]:
                    minQ.popleft()
                left += 1
            

        return longest


    def longestSubarray(self, nums, limit: int):
        maxLen, i = 0, 0
        minQueue = collections.deque([])
        maxQueue = collections.deque([])
        for j in range(len(nums)):
            while minQueue and minQueue[-1] > nums[j]:
                minQueue.pop()
            minQueue.append(nums[j])

            while maxQueue and maxQueue[-1] < nums[j]:
                maxQueue.pop()
            maxQueue.append(nums[j])
            
            if maxQueue[0] - minQueue[0] <= limit:
                maxLen = max(maxLen, j-i+1)
            else:
                if maxQueue[0] == nums[i]:
                    maxQueue.popleft()
                if minQueue[0] == nums[i]:
                    minQueue.popleft()
                i += 1
        return maxLen


sol = Solution()

print(sol.longestSubarray([2,2,2,4,4,2,5,5,5,5,5,2], 2))