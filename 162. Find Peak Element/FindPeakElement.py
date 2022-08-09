'''
https://leetcode.com/problems/find-peak-element/
'''


from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n < 3:
            max_val = max(nums)
            return nums.index(max_val)
        
        def binarySearchPeek(lo: int, hi: int) -> int:
            result = -1
            
            while lo <= hi:
                mid = (lo+hi)//2
                prev = (mid-1)
                nxt = (mid+1)

                if (prev < 0 or nums[mid] > nums[prev]) and (nxt >= n or nums[mid] > nums[nxt]):
                    return mid
                elif lo == hi-1:
                    lo = hi
                elif nums[prev] > nums[nxt]:
                    hi = mid
                else:
                    lo = mid
                
            return lo
                    
        return binarySearchPeek(0, n-1)