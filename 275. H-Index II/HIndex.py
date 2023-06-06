from typing import List


class Solution:
    # O(logn) time,
    # O(1) space,
    # Approach: binary search,
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        
        def findLowerBoundIndexToNum(lo, hi, num):
            while True:
                mid = (lo+hi)//2
                curr = citations[mid]
                
                if curr == num and (mid == 0 or citations[mid-1] < num):
                    return mid
                elif curr == num:
                    hi = mid-1
                elif curr > num:
                    if mid == 0 or citations[mid-1] < num:
                        return mid
                    hi = mid-1
                else:
                    if lo >= hi:
                        if citations[hi] >= num:
                            return hi
                        else:
                            return n
                    lo = mid+1
        
        def valid(hindex):
            index = findLowerBoundIndexToNum(0, n-1, hindex)
            citation_num = n - index
            return citation_num >= hindex
        
        
        def findMaxHindex(lo, hi):
            while True:
                mid = (lo+hi)//2
                validCitation = valid(mid)
                
                if validCitation and (mid == n or not valid(mid+1)):
                    return mid
                elif not validCitation:
                    hi = mid-1
                else:
                    if lo >= hi:
                        return hi
                    lo = mid+1
                
        return findMaxHindex(0, n)