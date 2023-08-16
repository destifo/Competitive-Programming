# O(nlogn) time,
# O(n) space,
# Approach: heap, design
import heapq


class SeatManager:

    def __init__(self, n: int):
        self.heap = [i+1 for i in range(n)]
        heapq.heapify(self.heap)
        

    def reserve(self) -> int:
        return heapq.heappop(self.heap)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)