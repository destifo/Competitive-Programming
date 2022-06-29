'''
https://leetcode.com/problems/furthest-building-you-can-reach/
'''


import heapq


class Solution:
    # had to sweat for this one, but a really interesting puzzle
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        max_heap = []
        i = 0
        while i < n-1 and (heights[i+1] - heights[i] <=0 or bricks >= 0):
            h_diff = heights[i+1] - heights[i]
            if h_diff <= 0:
                i +=1
                continue
            bricks -= h_diff
            heapq.heappush(max_heap, -h_diff)
            if bricks < 0 and ladders > 0:
                ladders -=1
                max_diff = -heapq.heappop(max_heap)
                bricks +=max_diff
            else:
                if bricks < 0:
                    return i
            i +=1

        return i

    
sol = Solution()
print(sol.furthestBuilding([1,2,4,7]
,3
,1))