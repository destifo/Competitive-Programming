from typing import List


class Solution:
    
    def findLessOrEqualToTarget(self, target, nums):
        
        lo = 0
        hi = len(nums)-1
        ans = len(nums)
        
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] > target:
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
                
        return ans
    
    
    
    # O(logn squared) time,
    # O(1) space,
    # Approach: binary search,
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = 1, arr[-1]+k
        ans = 1
        
        while lo <= hi:
            mid = (lo+hi)//2
            less_or_equal = self.findLessOrEqualToTarget(mid, arr)
            if mid == k + less_or_equal:
                ans = mid
                hi = mid-1
            elif mid < k + less_or_equal:
                lo = mid+1
            else:
                hi = mid-1
                
        return ans
    

    # O(n) time,
    # O(1) space,
    # Approach: two pointers
    def findKthPositive2(self, arr: List[int], k: int) -> int:
        
        n = 1
        i = 0
        while k > 0 and i < len(arr):
            if n == arr[i]:
                i += 1
                n += 1
            else:
                n += 1
                k -= 1
                
        return n + k-1