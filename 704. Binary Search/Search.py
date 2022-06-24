'''
https://leetcode.com/problems/binary-search/
'''

class Solution:
    # using recursion
    def search(self, nums, target: int):
        n = len(nums)
        mid = n//2
        def binarySearch(initial, index, final):
            if final - initial <=1 and (nums[final] != target and nums[initial] != target):
                return -1
            if nums[index] == target:
                return index
            elif nums[index] > target:
                return binarySearch(initial, (index - initial)//2 + initial, index)
            else:
                return binarySearch(index, (final - initial)//2 + index, final)
                
        return binarySearch(0, mid, n - 1)

    
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