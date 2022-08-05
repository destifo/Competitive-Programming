'''
https://leetcode.com/problems/find-the-duplicate-number/
'''


from typing import List


class Solution:
    # O(nlogn) time, 
    # O(1) space,
    # Approach: Binary search,
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        def countNumbersLessOrEqualToNum(num:int) -> int:
            count = 0
            for number in nums:
                if number <= num:
                    count +=1
                    
            return count
        
        def findDuplicate(start, end):
            mid = (start + end)//2
            count = countNumbersLessOrEqualToNum(mid)
            
            if count > mid and (mid == 1 or countNumbersLessOrEqualToNum(mid-1) == mid-1):
                return mid
            if start == end-1:
                return end
            if count > mid:
                return findDuplicate(start, mid)
            if count <= mid:
                return findDuplicate(mid, end)
            
        return findDuplicate(1, n)