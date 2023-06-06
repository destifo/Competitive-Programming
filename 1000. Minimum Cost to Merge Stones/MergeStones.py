'''
https://leetcode.com/problems/minimum-cost-to-merge-stones/
'''


import heapq


class Solution:
    # for non consecutive piles
    def mergeStones(self, stones: list[int], k: int):
        heapq.heapify(stones)
        min_cost = 0
        while len(stones) >= k:
            stone_sum = 0
            for i in range(k):
                stone_sum +=heapq.heappop(stones)
            
            min_cost += stone_sum
            heapq.heappush(stones, stone_sum)
            
        return min_cost if len(stones) == 1 else -1


sol = Solution()
print(sol.mergeStones([3,2,4,1], 2))