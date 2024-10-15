from collections import deque
import heapq
from typing import List, Set


class Solution:
    
    def calculatePoints(self, feedback: str, positives: Set[str], negatives: Set[str]) -> int:
        points = 0
        
        for word in feedback.split(" "):
            if word in positives:
                points += 3
            elif word in negatives:
                points -= 1
        
        return points
    
    
    # O(nlogn*k + m + o) time, n -> len(report), k -> len(report[i]), m -> len(positives), len(negatives)
    # O(n + m + o) space,
    # Approach: heap, deque
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        positives = set(positive_feedback)
        negatives = set(negative_feedback)
        
        heap = []
        for i in range(len(report)):
            feedback, student = report[i], student_id[i]
            
            student_points = self.calculatePoints(feedback, positives, negatives)

            if len(heap) == k:
                popped = heapq.heappop(heap)
                heapq.heappush(heap, max(popped, (student_points, -student)))
            else:
                heapq.heappush(heap, (student_points, -student))
        
        ans = deque()
        while heap:
            ans.appendleft(-heapq.heappop(heap)[1])
            
        return ans
