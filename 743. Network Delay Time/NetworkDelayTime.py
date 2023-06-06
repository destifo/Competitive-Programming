'''
https://leetcode.com/problems/network-delay-time/
'''

from collections import deque
import collections
import heapq



class Solution:
    # did 98% of it with a help
    def networkDelayTime(self, times, n: int, k: int):
        visited = set()
        minHeap = [(0, k)]
        neigbours = collections.defaultdict(list)
        for u, v, w in times:
            neigbours[u].append((v, w))

        time = 0
        while minHeap:
            w, v = heapq.heappop(minHeap)
            if v not in visited:
                time = max(w, time)
                visited.add(v)
                for neighbour, weight in neigbours[v]:
                    if neighbour not in visited:
                        heapq.heappush(minHeap, (weight + w, neighbour))

        return time

sol = Solution()
print(sol.networkDelayTime([[1,2,1],[2,1,3]],2,2))