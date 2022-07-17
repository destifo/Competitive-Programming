'''
https://leetcode.com/problems/intersection-of-multiple-arrays/
'''


class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        count = [0] * 1001
        n = len(nums)
        ans = []
        largest_num = 0
        
        for lst in nums:
            for num in lst:
                count[num] +=1
                largest_num = max(largest_num, num)
        
        for i in range(largest_num+1):
            if count[i] == n:
                ans.append(i)
                
        return ans