'''
https://leetcode.com/problems/first-bad-version/
'''


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n

        while end - start >=1:
            mid = (start + end) // 2
            if start == mid:
                if isBadVersion(start):   return start
                else:   return end
            if isBadVersion(mid) and not isBadVersion(mid-1):   return mid
            if not isBadVersion(mid):
                start = mid
            else:
                end = mid