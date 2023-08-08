'''
https://leetcode.com/problems/search-in-rotated-sorted-array/
'''


from typing import List


class Solution:
    # O(logn) time,
    # O(1) space,
    # Approach: binary search, recursive solution
    def search(self, nums: List[int], target: int) -> int:
        
        def findMinNumIndex(start, end):
            mid = (start + end)//2
            num = nums[mid]
            
            if nums[mid-1] > num and (mid == len(nums)-1 or num < nums[mid+1]):
                return mid
            if start == end-1:
                return end
            if num > nums[end]:
                return findMinNumIndex(mid, end)
            else:
                return findMinNumIndex(start, mid)
            
        
        def binarySearch(start, end):
            
            while True:
                mid = (start + end)//2
                num = nums[mid]
                if num == target:
                    return mid
                elif start >= end-1:
                    if nums[end] == target:
                        return end
                    return -1
                if num > target:
                    end = mid
                else:
                    start = mid
        
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        if n == 2:
            ans = 0 if nums[0] == target else -1
            if nums[1] == target:
                ans = 1
            return ans
        
        minNumIndex = findMinNumIndex(0, n-1)
        if target > nums[-1]:
            return binarySearch(0, minNumIndex-1)
        elif target == nums[-1]:
            return n-1
        else:
            return binarySearch(minNumIndex, n-2)


    # O(logn) time,
    # O(1) space,
    # Approach: binary search, iterative solution
    def search2(self, nums: List[int], target: int) -> int:
        
        def findMinNumIndex(start, end):
            
            while True:
                mid = (start + end)//2
                num = nums[mid]

                if nums[mid-1] > num and (mid == len(nums)-1 or num < nums[mid+1]):
                    return mid
                if start == end-1:
                    return end
                if num > nums[end]:
                    start = mid
                else:
                    end = mid

        
        def binarySearch(start, end):
            
            while True:
                mid = (start + end)//2
                num = nums[mid]
                if num == target:
                    return mid
                elif start >= end-1:
                    if nums[end] == target:
                        return end
                    return -1
                if num > target:
                    end = mid
                else:
                    start = mid
        
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        if n == 2:
            ans = 0 if nums[0] == target else -1
            if nums[1] == target:
                ans = 1
            return ans
        
        minNumIndex = findMinNumIndex(0, n-1)
        # print(minNumIndex)
        if target > nums[-1]:
            return binarySearch(0, minNumIndex-1)
        elif target == nums[-1]:
            return n-1
        else:
            return binarySearch(minNumIndex, n-2)
        
    
    # O(logn) time,
    # O(1) space,
    # Approach: binary search, one binary search solution
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target:
                return mid
            # for a target greater than the num at the mid index
            elif nums[mid] < target:
                # if the second half is the sorted part and the target is less than the num at the hi index or the first half is sorted, then we look into the second half
                if (nums[mid] < nums[hi] and target <= nums[hi]) or nums[lo] < nums[mid]:
                    lo = mid+1
                else:
                    hi = mid-1
            # for a target less than the num at the mid value
            else:
                # if the first half is the sorted part and the target is greater greater than the value at lo index or the second is sorted, then we search in the first half of the array
                if (nums[lo] <= nums[mid] and target >= nums[lo]) or nums[mid] < nums[hi]:
                    hi = mid-1
                else:
                    lo = mid+1
                    
        return -1


sol = Solution()
print(sol.search([4,5,6,7,0,1,2]
,4))