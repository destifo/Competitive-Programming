
from collections import defaultdict
from typing import List


class TweetCounts:
    
    # O(1) time,
    # O(1) space,
    # Approach: hashtable, 
    def __init__(self):
        self.records = defaultdict(list)
        self.time_mapping = {"minute": 59, "hour": 3599, "day": 86399}

    
    # O(1) time,
    # O(1) space,
    # Approach: hashtable, 
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.records[tweetName].append(time)
        
    def binarySearch(self, target, intervals):
        lo, hi = 0, len(intervals)-1
        
        if target < intervals[lo][0] or target > intervals[hi][1]:
            return hi+1
        
        while lo <= hi:
            mid = (lo+hi)//2
            
            if target >= intervals[mid][0] and target <= intervals[mid][1]:
                return mid
            elif target > intervals[mid][1]:
                lo = mid+1
            else:
                hi = mid-1
        
    
    # O(len(records[tweetName]) * log(len(intervals))) time,
    # O(len(intervals)) space,
    # Approach: binary search, 
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        ans = []
        intervals = []
        curr_interval = self.time_mapping[freq]
        curr_start = startTime
        curr_end = min(startTime+curr_interval, endTime)
        
        while curr_start <= endTime:
            ans.append(0)
            intervals.append((curr_start, curr_end))
            curr_start = curr_end + 1
            curr_end = min(curr_start+curr_interval, endTime)
            
        for record_time in self.records[tweetName]:
            interval_index = self.binarySearch(record_time, intervals)
            if interval_index < len(intervals):
                ans[interval_index] += 1
        
        return ans
        
        
# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)