import heapq


class KthLargest:
    
    def __init__(self, k: int, nums):
        self.minHeap = []
        nums.sort(reverse=True)
        length = min(k, len(nums))
        for i in range(length):
            num = nums[i]
            heapq.heappush(self.minHeap, num)
        self.k = k

    def add(self, val: int):
        if len(self.minHeap) < self.k or val > self.minHeap[0]:
            heapq.heappush(self.minHeap, val)
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)

        return self.minHeap[0]
        

kth = KthLargest(3,[4,5,8,2])
print(kth.add(3))
print(kth.add(5))

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)