# O(calls*logn) time,
# O(n) space,
# Approach: binary search, array
class SnapshotArray:

    def __init__(self, length: int):
        self.data = [[(0, 0)] for _ in range(length)]
        self.curr_snap = 0

        
    def set(self, index: int, val: int) -> None:
        self.data[index].append((self.curr_snap, val))
        

    def snap(self) -> int:
        self.curr_snap += 1
        return self.curr_snap-1
    
    
    def get(self, index: int, snap_id: int) -> int:
        index_data = self.data[index]
        
        lo, hi = 0, len(index_data)-1
        ans_index = 0
        
        while lo <= hi:
            mid = (lo+hi)//2
            if index_data[mid][0] <= snap_id:
                ans_index = mid
                lo = mid+1
            else:
                hi = mid-1
                
        return index_data[ans_index][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)