from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: prefix sum, sorting, greedy
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        combined = [(nums[i], cost[i]) for i in range(len(nums))]
        combined.sort()
        
        prefix_sum = [0]
        tot = 0
        
        for i in range(len(nums)):
            tot += combined[i][1]
            prefix_sum.append(tot)
            
        curr_cost = 0
        for i in range(1, len(nums)):
            diff = combined[i][0]-combined[0][0]
            curr_cost += (diff*combined[i][1])
            
        min_cost = curr_cost
        prev = combined[0][0]
        for i in range(1, len(nums)):
            diff = combined[i][0]-prev
            prev = combined[i][0]
            left_cost = prefix_sum[i]
            curr_cost += (diff*left_cost)
            right_cost = prefix_sum[len(nums)]-prefix_sum[i]
            curr_cost -= (diff*right_cost)
            min_cost = min(min_cost, curr_cost)
            
        return min_cost