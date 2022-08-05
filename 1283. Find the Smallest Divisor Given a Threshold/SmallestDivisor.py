'''
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
'''


from typing import List


class Solution:
    # O(nlogn) time,
    # O(1) space, 
    # Approach: binary search,
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def evalFunction(div):
            tot = 0
            for num in nums:
                qutnt = num//div
                tot +=qutnt
                if num % div != 0:
                    tot +=1
            
            return tot
        
        def binarySearch(start, end):
            mid = (start + end) // 2
            qutnt_sum = evalFunction(mid)
            if qutnt_sum <= threshold and (end-start < 2):
                return mid
            elif start >= end-1:
                return end
            elif qutnt_sum <= threshold:
                return binarySearch(start, mid)
            else:
                return binarySearch(mid, end)
            
        return binarySearch(1, max(nums))


sol = Solution()
print(sol.smallestDivisor([1,2,5,9]
,6))