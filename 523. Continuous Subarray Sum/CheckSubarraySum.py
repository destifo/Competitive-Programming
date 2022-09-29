from typing import List


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: prefix sum, two pointers, hashtable
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        for i in range(1, n):
            nums[i] += nums[i-1]
            
        def findSubarraySum(l: int, r: int) -> int:
            if l == 0:  return nums[r]
            
            return nums[r] - nums[l-1]
        
        
        vstd_mods = {0}
        l, r = 0, 1
        while r < n:
            tot = findSubarraySum(0, r)
            if tot % k in vstd_mods:
                return True
            
            tot_upto_left = findSubarraySum(0, l)
            mod = tot_upto_left % k
            
            vstd_mods.add(mod)
            l +=1
            r +=1
            
        return False