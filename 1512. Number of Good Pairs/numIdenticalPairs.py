'''
https://leetcode.com/problems/number-of-good-pairs/submissions/
'''


from collections import Counter
import math

class Solution:
    def calculate_combination(self, num1, num2):
        uppper = math.factorial(num1)
        lower = math.factorial(num2) * math.factorial(num1 - num2)
        return uppper//lower
    def numIdenticalPairs(self, nums) -> int:
        nums_count = Counter(nums)
        result = 0
        for num in nums_count:
            if nums_count[num] > 1:
                result += (self.calculate_combination(nums_count[num], 2))
        return result

sol = Solution()
print(sol.numIdenticalPairs([1,2,3,1,1,3]))