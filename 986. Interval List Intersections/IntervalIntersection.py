'''
https://leetcode.com/problems/interval-list-intersections/
'''


from typing import List


class Solution:
    # O(n + m) time,
    # O(n + m) space,
    # Approach: two pointers
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(firstList)
        m = len(secondList)
        
        def findIntersection(interval1: List[int], interval2: List[int]) -> List[int]:
            
            lower_bound = max(interval1[0], interval2[0])
            upper_bound = min(interval1[1], interval2[1])
            
            if lower_bound > upper_bound:
                return [lower_bound]
            
            return [lower_bound, upper_bound]
        
        
        i, j = 0, 0
        while i < n and j < m:
            interval1 = firstList[i]
            interval2 = secondList[j]
            intersection = findIntersection(interval1, interval2)
            higher_bound = intersection[-1]
            
            if len(intersection) > 1:
                ans.append(intersection) 
            
            if interval1[-1] > higher_bound:
                j+=1
            else:
                i +=1
                
        return ans