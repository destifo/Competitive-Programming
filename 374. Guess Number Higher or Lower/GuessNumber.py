# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return 0

class Solution:
    # O(logn) time,
    # O(1) space,
    # Approach: binary search, 
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n
        
        while lo <= hi:
            
            mid = (lo+hi)//2
            val = guess(mid)
            # print(mid, val)
            
            if val == 0: return mid
            elif val == -1: hi = mid-1
            else:   lo = mid+1
                
        return -1