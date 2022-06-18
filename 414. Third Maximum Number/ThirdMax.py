'''
https://leetcode.com/problems/third-maximum-number/
'''


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