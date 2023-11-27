'''
https://leetcode.com/problems/remove-element/
'''

from typing import List


class Solution:
    def removeElement(self, nums, val: int):
        n = len(nums)
        if n == 0:
            return 0
        
        def swap(lst, ind1, ind2):
            temp = lst[ind1]
            lst[ind1] = lst[ind2]
            lst[ind2] = temp
            
        l, r = 0, n - 1
        while l < r:
            if nums[r] == val:
                r -=1
            else:
                if nums[l] == val:
                    swap(nums, l, r)
                    r -=1        
                l +=1
                
        return r if nums[r] == val else r + 1
    
    
    def getLast(self, val: int, index: int, nums: List[int]) -> int:
        while index >= 0 and nums[index] == val:
            index -= 1
            
        return index
    
    
    # O(n) time,
    # O(1) space,
    # Approach: two pointers, 
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        last = self.getLast(val, n-1, nums)
        
        i = 0
        while i < last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last = self.getLast(val, last-1, nums)
            i += 1
            
        return last+1