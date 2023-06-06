'''
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
'''


class Solution:
    # O(mlog(mn)) time,
    # O(1) space,
    # Approach: binary search,
    def findKthNumber(self, m: int, n: int, k: int) -> int:
 
        def countNumsLessOrEqual(num:int) -> int:
            count = 0
            for i in range(1, m+1):
                count += min(num//i, n)
                
            return count
        
        
        def binarySearch(low, high) -> int:
            mid = (low + high)//2
            count = countNumsLessOrEqual(mid)
            
            if low >= high:
                return mid
            elif count >= k:
                return binarySearch(low, mid)
            else:
                return binarySearch(mid+1, high)
            
        return binarySearch(1, m*n)