from typing import List


class Solution:
    
    def findIndex(self, target: int, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        ans = len(nums)
        
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] >= target:
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
                
        return ans
    
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: prefix sum, binary search, math
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = [0]
        tot = 0
        for num in nums:
            tot += num
            prefix_sum.append(tot)
            
        answer = []
        for query in queries:
            ops = 0
            index = self.findIndex(query, nums)
            left_part = prefix_sum[index]
            right_part = prefix_sum[len(nums)]-prefix_sum[index]
            ops += query*index - left_part
            ops += right_part - query*(len(nums)-index)
            answer.append(ops)
            
        return answer
    '''
    - [1, 3, 6, 8] => [1, 1, 1, 1], 0+2+5+7 = 14, 
            0, -2, -5, -7 -> 4, 2, -1, -3
            4*(2) + 4(5)
            (5-1) + (5-3) + (6-5) + (8-5)
            (5-1+5-3) + (6-5+8-5)
            5*2 - (1+3) + (-5*2 + (5+8))
            ((query*index) - left_part) + (right_part -query*(legth-index))
            10*3 - 11 + 
    - [1, 3, 6, 8] => [5, 5, 5, 5], 4+2+1+3 = 10
    '''