from typing import List


class Solution:
    # naive approach
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        minCostAt = [-1] * n


        def findminCost(stair, currCost):
            if stair >= n:
                return currCost

            if stair == n - 1:
                currCost +=cost[stair]
                return currCost

            currCost += cost[stair]
            return min(findminCost(stair + 1, currCost), findminCost(stair + 2, currCost))

        return min(findminCost(0, 0), findminCost(1, 0))

    
    def minCostClimbingStairs2(self, cost):
        # very efficent approach using iterative solution 
        n = len(cost)
        minCostAt = [-1] * n
        minCostAt[n - 1] = cost[n - 1]
        minCostAt[n - 2] = cost[n - 2]

        i = n - 3
        while i > -1:
            minCostAt[i] = cost[i] + min(minCostAt[i + 1], minCostAt[i + 2])
            i -=1

        return min(minCostAt[0], minCostAt[1])

    
    def minCostClimbingStairs3(self, cost):
        # very efficent approach by updating the cost list 
        n = len(cost)

        i = n - 3
        while i > -1:
            cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])
            i -=1

        return min(cost[0], cost[1])

    
    # O(n) time,
    # O(n) space,
    # Approach: dp, tabulation
    def minCostClimbingStair4(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        table = [0 for i in range(n)]
        
        table[0] = cost[0]
        table[1] = cost[1]
        
        for i in range(2, n-1):
            table[i] = min(table[i-1], table[i-2]) + cost [i]
        table[n-1] = min(table[n-2], (table[n-3]+cost[n-1]))
        return table[n-1]
