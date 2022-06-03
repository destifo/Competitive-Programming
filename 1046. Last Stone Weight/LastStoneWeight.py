'''
https://leetcode.com/problems/last-stone-weight/
'''
import heapq


class Solution:
    def lastStoneWeight(self, stones):
        minHeap = []
        for stone_weight in stones:
            heapq.heappush(minHeap, -stone_weight)

        while len(minHeap) > 1:
            heavy_stone1 = abs(heapq.heappop(minHeap))
            heavy_stone2 = abs(heapq.heappop(minHeap))

            diff = heavy_stone2 - heavy_stone1
            if diff:
                heapq.heappush(minHeap, diff)

        return -heapq.heappop(minHeap) if minHeap else 0
