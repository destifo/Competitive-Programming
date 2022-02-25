'''
https://leetcode.com/problems/top-k-frequent-elements/
'''


from audioop import reverse
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k: int):
        nums_len = len(nums)

        nums_count = Counter(nums)

        nums_count = sorted(nums_count.items(), key=lambda x:x[1], reverse=True)

        result = []
        i = 0

        for i in range(k):
            result.append(nums_count[i][0])
        
        return result


sol = Solution()

print(sol.topKFrequent(nums = [1], k = 1))