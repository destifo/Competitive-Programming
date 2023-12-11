from collections import defaultdict
import math
from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: hash map, 
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = defaultdict(int)
        
        max_freq = 0
        ans = arr[0]
        for num in arr:
            count[num] += 1
            if count[num] > max_freq:
                ans = num
                max_freq = count[num]
            
        return ans
    
    
    # O(n) time,
    # O(1) space,
    # Approach: sliding window, 
    def findSpecialInteger(self, arr: List[int]) -> int:
        curr_count = 1
        
        max_freq = 0
        ans = arr[0]
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                if max_freq < curr_count:
                    max_freq = curr_count
                    ans = arr[i-1]
                curr_count = 1
            else:
                curr_count += 1
        if curr_count > max_freq:
            ans = arr[-1]
            
        return ans
    
    
    def findFirst(self, lo: int, hi: int, nums: List[int]) -> int:
        index = hi
        hi -= 1
        target = nums[index]
        
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] >= target:
                index = mid
                hi = mid-1
            else:
                lo = mid+1
                
        return index
    
    
    def findLast(self, lo: int, hi: int, nums: List[int]) -> int:
        index = lo
        lo += 1
        target = nums[index]
        
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] <= target:
                index = mid
                lo = mid+1
            else:
                hi = mid-1
                
        return index
    
    
    
    def findFreq(self, index: int, nums: List[int]) -> int:
        
        start = self.findFirst(0, index, nums)
        end = self.findLast(index, len(nums)-1, nums)
        
        return (end-start)+1
    
    
    
    # O(logn) time,
    # O(1) space,
    # Approach: binary search, 
    def findSpecialInteger(self, arr: List[int]) -> int:
        ans = arr[0]
        
        quart = math.ceil(len(arr)/4)
        index = quart
        
        max_freq = 1
        while index < len(arr):
            freq = self.findFreq(index, arr)
            if freq > max_freq:
                max_freq = freq
                ans = arr[index]
            index += quart
            
        return ans