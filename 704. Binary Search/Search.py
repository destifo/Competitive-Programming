'''
https://leetcode.com/problems/binary-search/
'''

class Solution:
    # using recursion
    def search(self, nums, target: int):
        n = len(nums)
        
        def binary_search(start, end):
            mid = (start + end) // 2
            if nums[mid] == target: return mid
            if start == mid:    return end if target == nums[end] else -1
            if nums[mid] > target:
                return binary_search(start, mid)
            else:
                return binary_search(mid, end)
            
        return binary_search(0, n-1)

    
    # using a loop
    def search2(self, nums: list[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if target == nums[0] else -1
        
        start = 0
        end = n-1
        while end - start >= 1:
            mid = (start + end) //2
            if nums[mid] == target:
                return mid
            if end-start == 1:
                if nums[end] == target:
                    return mid + 1
                else:
                    return -1
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
                
        return -1