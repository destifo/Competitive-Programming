from typing import List


class Solution:
    # O(numCourses) time,
    # O(numCourses) space,
    # Approach: DFS, hashmap
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        required = [[] for i in range(numCourses)]
        possible_courses = set()
        vstd = set()
        
        for course, required_course in prerequisites:
            required[course].append(required_course)
            
        
        def isPossible(course_no: int) -> bool:
            if course_no in possible_courses:
                return True
            
            if course_no in vstd:
                return False
            
            vstd.add(course_no)
            for required_course in required[course_no]:
                if not isPossible(required_course):
                    return False
                possible_courses.add(required_course)
            
            possible_courses.add(course_no)
            return True
        
        for i in range(numCourses):
            vstd = set()
            if not isPossible(i):
                return False
            possible_courses.add(i)
            
        return True


sol = Solution()
print(sol.canFinish(3
,[[0,1],[0,2],[1,2]]))