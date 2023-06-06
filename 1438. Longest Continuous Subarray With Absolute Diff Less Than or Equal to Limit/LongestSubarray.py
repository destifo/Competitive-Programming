"""
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/submissions/
"""

import collections
from typing import List


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

    
    # O(n) time,
    # O(n) space,
    # Approach: monotonic queue, deque
    def longestSubarray3(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        curr_max = collections.deque()
        curr_max.append(nums[0])
        curr_min = collections.deque()
        curr_min.append(nums[0])
        max_len = 1
        
        l, r = 0, 1
        while r < n:
            num = nums[r]
            while curr_max and num > curr_max[-1]:
                curr_max.pop()
                
            while curr_min and num < curr_min[-1]:
                curr_min.pop()
                
            curr_min.append(num)
            curr_max.append(num)
            
            max_len = max(max_len, r-l)
            while abs(curr_max[0] - curr_min[0]) > limit:
                if nums[l] == curr_max[0]:
                    curr_max.popleft()
                if nums[l] == curr_min[0]:
                    curr_min.popleft()
                    
                l +=1
                
            r +=1
        
        max_len = max_len = max(max_len, r-l)
        return max_len
    

    # O(len(nums)) time,
    # O(len(nums)) space,
    # Approach: monotonic queue,
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc_queue = collections.deque()
        dec_queue = collections.deque()
        
        ans = 1
        
        left, right = 0, 0
        
        while right < len(nums):
            num = nums[right]
            
            while inc_queue and inc_queue[-1] > num:
                inc_queue.pop()
                
            while dec_queue and dec_queue[-1] < num:
                dec_queue.pop()
            
            inc_queue.append(num)
            dec_queue.append(num)
            right += 1
            
            while dec_queue and inc_queue and dec_queue[0] - inc_queue[0] > limit:
                first_num = nums[left]
                left += 1
                if first_num == dec_queue[0]:
                    dec_queue.popleft()
                elif first_num == inc_queue[0]:
                    inc_queue.popleft()
                
            ans = max(ans, right-left)
            
        
        return ans


sol = Solution()

print(sol.longestSubarray([2,2,2,4,4,2,5,5,5,5,5,2], 2))