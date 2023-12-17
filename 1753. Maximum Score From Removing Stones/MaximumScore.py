import heapq


class Solution:
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: heap, greedy
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        heapq.heapify(heap)
        score = 0
        
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            curr_score = 0
            if heap:
                if -heap[0] != second:
                    curr_score = second+heap[0]
                else:
                    curr_score = 1
            else:
                curr_score = second
                
            first -= curr_score
            second -= curr_score
            score += curr_score
            if first > 0:
                heapq.heappush(heap, -first)
                
            if second > 0:
                heapq.heappush(heap, -second)
                
        return score