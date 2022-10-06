# O(calls) time, calls --> number of method calls
# O(s) space, s --> number of 'set' method calls,
# Approach: hashtables, binary search
class TimeMap:

    def __init__(self):
        self.map = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
            
        self.map[key].append((timestamp, value))
    
    def get(self, key: str, timestamp: int) -> str:
        val = ""
        
        def binarySearch(lo: int, hi: int, timestamps) -> int:
            ans = lo
            while lo<=hi:
                mid = lo + (hi+lo)
                
                if timestamps[mid][0] <= timestamp:
                    ans = mid
                    lo = mid+1
                else:
                    hi = mid-1
            
            return ans
        
        if key in self.map and (self.map[key][0][0] <= timestamp):
            val_index = binarySearch(0, len(self.map[key])-1, self.map[key])
            val = self.map[key][val_index][1]
            
        return val


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)