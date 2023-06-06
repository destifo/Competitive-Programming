'''
https://leetcode.com/problems/third-maximum-number/
'''


from typing import List


class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        vstd = set()
        distnict_count = 0
        for i in range(n-1,-1,-1):
            num = nums[i]
            if num in vstd:
                continue
            distnict_count +=1
            if distnict_count == 3: return num
            vstd.add(num)
            
        return nums[-1]


    # O(n) time,
    # O(1) space,
    # Approach: array, 
    def thirdMax2(self, nums: List[int]) -> int:
        first_max = float('-inf')
        second_max = float('-inf')
        third_max = float('-inf')
        
        for num in nums:
            if num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif num > second_max and num != first_max:
                third_max = second_max
                second_max = num
            elif num > third_max and num != second_max and num != first_max:
                third_max = num
                
        return third_max if third_max != float('-inf') else first_max