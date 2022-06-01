'''
https://leetcode.com/problems/binary-search/
'''

class Solution:
    def search(self, nums, target: int):
        n = len(nums)
        mid = n//2
        def binarySearch(initial, index, final):
            if final - initial <=1 and (nums[final] != target and nums[initial] != target):
                return -1
            if nums[index] == target:
                return index
            elif nums[index] >= target:
                return binarySearch(initial, (index - initial)//2 + initial, index)
            else:
                return binarySearch(index, (final - initial)//2 + index, final)
                
        return binarySearch(0, mid, n - 1)