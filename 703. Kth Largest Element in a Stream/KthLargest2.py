'''
https://leetcode.com/problems/kth-largest-element-in-a-stream/
'''


import heapq


class KthLargest:

    # O(nlogn) time,
    # O(k) space, 
    # Approach: heap, sorting
    def __init__(self, k: int, nums):
        self.min_heap = []
        self.k = k
        nums.sort(reverse=True)
        
        for num in nums:
            if self.heapLength() < k:
                self.heappush(num)
            else:
                break
                
    def heapLength(self) -> int:
        return len(self.min_heap)
    
    
    def heapPeek(self) -> int:
        return self.min_heap[0]
    
    
    def heappush(self, val:int) -> None:
        heapq.heappush(self.min_heap, val)
        
    
    def heappop(self) -> int:
        return heapq.heappop(self.min_heap)
                       

    # O(logn) time,
    # O(1) space, 
    # Approach: heap,
    def add(self, val: int):
        if self.heapLength() < self.k:
            self.heappush(val)
        elif val > self.heapPeek():
            num = self.heappop()
            num = max(num, val)
            self.heappush(val)
            
        return self.heapPeek()
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)