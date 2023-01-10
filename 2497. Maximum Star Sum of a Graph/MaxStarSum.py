from collections import defaultdict
from typing import List


class Solution:
    
    def getMaxSum(self, nums, k):
        tot = 0
        for i in range(len(nums)):
            if nums[i] < 0 or k <= 0: return tot
            k -= 1
            tot += nums[i]
            
        return tot
    
    
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for edge in edges:
            nod1, nod2 = edge
            graph[nod1].append(vals[nod2])
            graph[nod2].append(vals[nod1])
            
        max_sum = vals[0]
        for node in range(len(vals)):
            nbrs = graph[node]
            nbrs.sort(reverse=True)
            max_sum = max(max_sum, self.getMaxSum(nbrs, k)+vals[node])

        return max_sum