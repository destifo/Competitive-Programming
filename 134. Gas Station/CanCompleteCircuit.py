'''
https://leetcode.com/problems/gas-station/
'''


class Solution:
    # O(n^2) time, brute force solution(naive)
    # O(1) space
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        
        for i in range(n):
            if cost[i] > gas[i]:    continue
            curr_station = i
            tot_gas = 0
            travel_distance = 0
            while travel_distance <= n and tot_gas >= 0:
                tot_gas += gas[curr_station]
                tot_gas -= cost[curr_station]
                curr_station +=1
                curr_station %=n
                travel_distance +=1
            
            if tot_gas >= 0 and travel_distance:
                return i
            
        return -1  


    # O(n) time, only traverses the array one time
    # O(1) space, no extra space used except for the variables
    def canCompleteCircuit2(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        # means no solution exits, 
        # we dont have enough gas to complete a circle
        if sum(gas) < sum(cost):
            return -1

        tot = 0
        start_station = 0
        for i in range(n):
            tot += (gas[i] - cost[i])

            # we basically search for the first index 
            # where the tot goes on without falling below zero
            if tot < 0:
                tot = 0
                start_station = i + 1
            
        return start_station