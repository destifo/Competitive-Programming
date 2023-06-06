from typing import List


class Solution:
    
    def findGreaterThanDoubleOfTarget(self, nums: List[int], target: int) -> int:
        
        lo, hi = 0, len(nums)-1
        ans = -1
        while lo <= hi:
            mid = (lo+hi)//2
            if target > (2 * nums[mid]):
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
                
        return ans
    
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        while i < len(left):
            result.append(left[i])
            i += 1
            
        while j < len(right):
            result.append(right[j])
            j += 1
                
        return result
    
    
    def mergeSort(self, nums: List[int]) -> List[int]:
        
        if len(nums) < 2:
            return nums
        
        mid = len(nums)//2
        
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        
        for i in range(len(left)):
            curr_num = left[i]
            count = self.findGreaterThanDoubleOfTarget(right, curr_num) + 1
            self.pairs += count
        
        return self.merge(left, right)
    
    
    # O(nlogn^2) time,
    # O(nlogn) space,
    # Approach: merge sort, binary search, divide and conquer, 
    def reversePairs(self, nums: List[int]) -> int:
        self.pairs = 0
        
        self.mergeSort(nums)
        return self.pairs