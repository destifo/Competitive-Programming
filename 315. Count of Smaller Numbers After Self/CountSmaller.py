from typing import List


class Solution:
    
    def countSmallerThanTarget(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        ans = -1
        
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid][0] < target:
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
                
        return ans + 1
        
    
    def mergeSort(self, nums: List[int]) -> List[int]:
        
        if len(nums) < 2:
            return nums
        
        mid = len(nums)//2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        
        for i in range(len(left)):
            self.count[left[i][1]] += self.countSmallerThanTarget(right, left[i][0])
        
        return self.merge(left, right)
    
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        
        result = []
        
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i][0] < right[j][0]:
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
    
    
    # O(nlogn) time,
    # O(nlogn) space,
    # Approach: merge sort, divide and conquer, binary search
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.count = [0 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            nums[i] = (num, i)
        
        self.mergeSort(nums)
        return self.count