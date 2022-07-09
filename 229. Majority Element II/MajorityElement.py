'''
https://leetcode.com/problems/majority-element-ii/
'''


class Solution:
    # O(n) time
    # O(n) space
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = []
        nums_count = dict()
        
        for num in nums:
            count = nums_count.get(num, 0)
            if count == 'added':
                continue
            nums_count[num] = count + 1
            if nums_count[num] > n // 3:
                result.append(num)
                nums_count[num] = 'added'
                
        return result