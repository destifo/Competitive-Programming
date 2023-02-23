from typing import List


class Solution:
    
    # O(n^2) time, 
    # O(n*m) space, m -> the max diff between two nums
    # Approach: top down dp, 
    def longestArithSeqLength(self, nums: List[int]) -> int:
        memo = {}
        longest = 0
        
        for i in range(len(nums)-2, -1, -1):
            num = nums[i]
            for j in range(i+1, len(nums)):
                next_num = nums[j]
                diff = next_num-num
                if (i, diff) in memo:
                    continue
                # print(j, diff)
                # print(memo)
                if (j, diff) in memo:
                    memo[(i, diff)] = (memo[(j, diff)] + 1)
                else:
                    memo[(i, diff)] = 2
                
                longest = max(longest, memo[(i, diff)])

        return longest