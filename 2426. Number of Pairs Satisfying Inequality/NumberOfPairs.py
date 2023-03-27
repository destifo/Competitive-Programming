from typing import List


class Solution:
    
    def findGreaterOrEqual(self, nums, target):
        
        lo, hi = 0, len(nums)-1
        ans = len(nums)
        
        while lo <= hi:
            mid = (lo+hi)//2
            
            if nums[mid] >= target:
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
                
        return ans
    
    
    
    def mergeSort(self, nums):
        if len(nums) < 2:
            return nums
        
        mid = len(nums)//2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        for i in range(len(left)):
            curr_val = left[i]
            count = len(right) - self.findGreaterOrEqual(right, curr_val-self.diff)
            self.ans += count

        return self.merge(left, right)
    
    
    def merge(self, left, right):
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
    
    
    # O(nlogn^2) time,
    # O(nlogn) space,
    # Approach: merge sort, divide and conquer, binary search
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.ans = 0
        self.diff = diff
        
        nums1 = [nums1[i]-nums2[i] for i in range(len(nums1))]
        self.mergeSort(nums1)
        
        return self.ans