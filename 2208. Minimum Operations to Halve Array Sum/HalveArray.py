class Solution:
    
    # O(n + stepslogn) time,
    # O(n) space,
    # Approach: heap, greedy, 
    def halveArray(self, nums: List[int]) -> int:
        
        heap = []
        total = 0
        for num in nums:
            total += num
            heapq.heappush(heap, -num)
        
        half = total/2
        steps = 0
        while total > half:
            steps += 1
            popped = -heapq.heappop(heap)
            popped /= 2
            total -= popped
            heapq.heappush(heap, -popped)
            
        return steps