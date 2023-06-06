'''
https://leetcode.com/problems/remove-element/
'''

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