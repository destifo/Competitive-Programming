from typing import List


class Solution:
    
    def findPossibleMax(self, lo: int, target: int, nums: List[int]) -> int:
        ans = lo-1
        
        hi = len(nums)-1
        
        while lo <= hi:
            mid = (lo+hi)//2
            num = nums[mid]
            
            if num <= target:
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
                
        return ans+1
    
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: binary search, sorting, math
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = (10**9) + 7
        count = 0
        nums.sort()
        
        for index, num in enumerate(nums):
            if (num*2) > target:
                break
            possible_max_index = self.findPossibleMax(index+1, target-num, nums)
            size = possible_max_index-index
            curr_count = size
            if size >= 2:
                curr_count = 2**(size-1)
            count += curr_count
            count %= MOD
            
        return count
    

    # O(nlogn) time,
    # O(1) space,
    # Approach: sorting, two pointers, 
    def numSubseq2(self, nums: List[int], target: int) -> int:
        MOD = (10**9) + 7
        lo, hi = 0, len(nums)-1
        count = 0
        nums.sort()
        
        while lo <= hi:
            
            if nums[lo]+nums[hi] <= target:
                size = (hi-lo)+1
                count += 2**(size-1)
                count %= MOD
                lo += 1
            else:
                hi -=1
                
        return count