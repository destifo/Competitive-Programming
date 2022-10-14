from collections import defaultdict
from typing import List


class Solution:
    # O(numCourse) time, 
    # O(numCourse) space,
    # Approach: topological order, dfs coloring
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        required = defaultdict(list)
        
        for course, required_course in prerequisites:
            required[course].append(required_course)
        
        colors = [0 for _ in range(numCourses)]
        topological_order = []
        def hasCycle(curr: int) -> bool:
            if colors[curr] == 2:
                return False
            
            if colors[curr] == 1:
                return True
            
            colors[curr] = 1
            
            for nb in required[curr]:
                if hasCycle(nb):    return True
            
            colors[curr] = 2
            topological_order.append(curr)
            return False
        
        for course in range(numCourses):
            if hasCycle(course):    return []
            
        return topological_order