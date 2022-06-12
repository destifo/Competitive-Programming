'''
https://leetcode.com/problems/divide-array-into-equal-pairs/
'''


from collections import Counter


class Solution:
    def divideArray(self, nums: list):
        nums_count = Counter(nums)
        
        for val in nums_count.values():
            if val % 2 != 0:    return False
            
        return True