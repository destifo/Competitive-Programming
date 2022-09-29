from collections import deque
from typing import List


class Solution:
    # O(logn + k) time,
    # O(k) space,
    # Approach: Binary, two pointers, queue
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = deque()
        
        def binarySearch(num: int, arr: List[int]) -> int:
            lo, hi = 0, len(arr)-1
            
            while lo <= hi:
                mid = (hi+lo)//2
                curr_num = arr[mid]
                if curr_num == num:
                    return mid
                
                elif curr_num > num:
                    hi = mid-1
                else:
                    lo = mid+1
                        
            return lo
        
        num_index = binarySearch(x, arr)
        l, r = num_index-1, num_index
        n = len(arr)
        
        while l >= 0 or r < n:
            if len(ans) == k:
                break
                
            left_estimate = float('inf')
            if l >= 0:
                left_estimate = abs(arr[l]-x)
            
            right_estimate = float('inf')
            if r < n:
                right_estimate = abs(arr[r]-x)
            
            if left_estimate > right_estimate:
                ans.append(arr[r])
                r +=1
            else:
                ans.appendleft(arr[l])
                l -=1
                
        return ans