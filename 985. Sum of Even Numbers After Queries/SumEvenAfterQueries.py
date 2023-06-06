'''
https://leetcode.com/problems/sum-of-even-numbers-after-queries/
'''


from typing import List


class Solution:
    # O(n+q) time, q --> len(queries), n --> len(nums)
    # O(q) space,
    # Approach: simulation, 
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        ans = []
        
        for num in nums:
            if num % 2 == 0:
                even_sum += num
        
        for query in queries:
            val, index = query
            result = nums[index] + val
            if nums[index] % 2 == 0:
                even_sum -=nums[index]
            
            if result % 2 == 0:
                even_sum += result
                    
            nums[index] = result
            ans.append(even_sum)
            
        return ans