'''
https://leetcode.com/problems/kth-largest-element-in-an-array/
'''


class Solution:
    # straight forward soln, but have to do it the other way around
    def findKthLargest(self, nums: list[int], k: int):
        nums.sort()
        return nums[-k]