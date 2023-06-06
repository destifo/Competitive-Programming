'''
https://leetcode.com/problems/majority-element/
'''


class Solution:
    # O(n) time complexity, but one interesting fact is that the algorithm will 
    # finish before the whole array is traveresed if the majority element does hit
    #  greater than n // 2 before the array is finished traversing
    # O(n) space complexity, for the map
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        nums_count = dict()
        
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
            if nums_count[num] > n // 2:
                return num
        
        return -1