import heapq


class SmallestInfiniteSet:
    
    # O(max_numlogmax_num) time,
    # O(max_num) space,
    # Approach: hashmap, heap
    def __init__(self):
        self.exists = [True for _ in range(1001)]
        self.nums = [i+1 for i in range(1000)]
        heapq.heapify(self.nums)
        

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.nums)
        self.exists[smallest] = False
        
        return smallest
        

    def addBack(self, num: int) -> None:
        if self.exists[num]:
            return
        
        self.exists[num] = True
        heapq.heappush(self.nums, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)