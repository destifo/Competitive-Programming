from typing import List


class Solution:
    
    def binarySearch(self, start, target, intervals):
        end = len(intervals)-1
        ans = None
        
        while start <= end:
            mid = (start+end)//2
            
            if intervals[mid][0] >= target:
                ans = intervals[mid][0]
                end = mid-1
            else:
                start = mid+1
        
        return ans
    
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: binary search, array, 
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        index_of = {intervals[i][0]:i for i in range(len(intervals))}
        intervals.sort()
        ans = [-1 for _ in range(len(intervals))]
        
        for i, interval in enumerate(intervals):
            result = self.binarySearch(i, interval[1], intervals)
            if result != None:
                result = index_of[result]
            else:
                result = -1
                
            ans[index_of[interval[0]]] = result

        return ans