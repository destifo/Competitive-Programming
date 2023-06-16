from typing import List


class Solution:
    
    def findDiffAfterMutation(self, value: int, arr: List[int], prefix_sum: List[int]) -> int:
        
        lo, hi = 0, len(arr)-1
        index = -1
        while lo <= hi:
            mid = (lo+hi)//2
            if arr[mid] <= value:
                index = mid
                lo = mid+1
            else:
                hi = mid-1
                
        tot = prefix_sum[index+1]
        mutated_len = len(arr)-index-1
        tot += (value*mutated_len)
        
        return tot
                
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: prefix sum, binary search, sorting, 
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        prefix_sum = [0]
        tot = 0
        for num in arr:
            tot += num
            prefix_sum.append(tot)
        
        min_diff = float('inf')
        ans = arr[-1]
        for i in range(0, arr[-1]+1):
            curr_diff = abs(target-self.findDiffAfterMutation(i, arr, prefix_sum))
            if curr_diff > min_diff:
                break
            elif curr_diff < min_diff:
                ans = i
                min_diff = curr_diff
                
        return ans