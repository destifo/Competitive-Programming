'''
https://leetcode.com/problems/longest-happy-string/
'''

from collections import deque
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int):
        maxHeap = []
        if a:   heapq.heappush(maxHeap, (-a, 'a'))
        if b:   heapq.heappush(maxHeap, (-b, 'b'))
        if c:   heapq.heappush(maxHeap, (-c, 'c'))

        waiting_queue = deque()

        result = ''
        while maxHeap:
            count, ch = heapq.heappop(maxHeap)
            count *=-1

            result+=ch
            count -=1
            if waiting_queue:
                curr = waiting_queue.popleft()
                heapq.heappush(maxHeap, curr)
            
            if count > 0 and (len(result) > 1 and ( result[-1] == ch and result[-2] == ch)):
                waiting_queue.append((-count, ch))
            else:
                if count > 0:
                    heapq.heappush(maxHeap, (-count, ch))
            

        return result


sol = Solution()
print(sol.longestDiverseString(0,8,11))