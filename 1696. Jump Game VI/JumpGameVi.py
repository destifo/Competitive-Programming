from collections import deque
import collections
from typing import Deque



class Solution:
    def maxResult(self, nums, k: int):
        qu = collections.deque()
        n = len(nums)
        dp = [None] * n
        dp[n - 1] = nums[n - 1]
        qu.append(n - 1)

        for i in range(n - 2, -1, -1):
            if qu and qu[0] - i> k:
                qu.popleft()
            dp[i] = nums[i] + dp[qu[0]]
            while qu and dp[qu[-1]] < dp[i]:
                qu.pop()
            qu.append(i)

        return dp[0]


sol = Solution()
print(sol.maxResult([10,-5,-2,4,0,3], k = 3))