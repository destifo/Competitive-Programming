'''
https://leetcode.com/problems/find-median-from-data-stream/
'''


import heapq


class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        if not self.is_equalized():
            self.equalize()
            
        if len(self.right) >= 1 and self.right[0] < -self.left[0]:
            # print('yes')
            self.swap()
        
        
    def swap(self):
        val = -heapq.heappop(self.left)
        val2 = -heapq.heappop(self.right)
        
        heapq.heappush(self.right, val)
        heapq.heappush(self.left, val2)
        
    
    def equalize(self):
        val = -heapq.heappop(self.left)
        heapq.heappush(self.right, val)

    
    def size(self):
        return len(self.right) + len(self.left)

    
    def is_equalized(self):
        return len(self.left) - len(self.right) < 2


    def findMedian(self) -> float:
        median = None
        if self.size() % 2 == 0:
            if len(self.right) != 0:
                median = (self.right[0] + -self.left[0]) / 2
            else:
                median = (-self.left[1] + -self.left[0]) / 2
        else:
            median = float(-self.left[0])

        return median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()