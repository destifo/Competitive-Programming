from collections import defaultdict, deque
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


    # O(numCourse) time, 
    # O(numCourse) space,
    # Approach: topological order, bfs
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incomings = [0 for _ in range(numCourses)]
        
        for course, required_course in prerequisites:
            graph[required_course].append(course)
            incomings[course] +=1
        
        topological_order = []
        qu = deque()
        for course in range(numCourses):
            if incomings[course] == 0:  qu.append(course)
                
        while qu:
            qu_len = len(qu)
            for _ in range(qu_len):
                course = qu.popleft()
                topological_order.append(course)
                
                for required in graph[course]:
                    incomings[required] -=1
                    if incomings[required] == 0:
                        qu.append(required)
                        
        return [] if len(topological_order) != numCourses else topological_order