'''
https://leetcode.com/problems/minimum-time-to-complete-trips/
'''


from typing import List


class Solution:
    # O(nlogn) time,
    # O(1) space,
    # Approach: binary search, recursive solution
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def calcTotalTrips(t:int) -> int:
            tot_trips = 0
            for bus_time in time:
                tot_trips += (t//bus_time)
                
            return tot_trips
        
        
        def findMinTime(start:int, end:int) -> int:
            mid = (start + end) // 2
            tot_trips = calcTotalTrips(mid)
            
            if tot_trips == totalTrips and (mid == 1 or calcTotalTrips(mid-1) < totalTrips):
                return mid
            if start == end - 1:
                return end
            if tot_trips >= totalTrips:
                return findMinTime(start, mid)
            else:
                return findMinTime(mid, end)
            
        return findMinTime(1, min(time) * totalTrips)

    
    # O(nlogn) time,
    # O(1) space,
    # Approach: binary search, iterative solution
    def minimumTime2(self, time: List[int], totalTrips: int) -> int:

        def calcTotalTrips(t:int) -> int:
            tot_trips = 0
            for bus_time in time:
                tot_trips += (t//bus_time)
                
            return tot_trips
        
        start = 1
        end = min(time) * totalTrips
        while True:
            mid = (start + end) // 2
            tot_trips = calcTotalTrips(mid)
            
            if tot_trips == totalTrips and (mid == 1 or calcTotalTrips(mid-1) < totalTrips):
                return mid
            if start == end - 1:
                return end
            if tot_trips >= totalTrips:
                end = mid
            else:
                start = mid


sol = Solution()
print(sol.minimumTime([1,2,3]
,5))