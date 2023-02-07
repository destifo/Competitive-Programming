from collections import defaultdict


class Solution:
    
    # O(len(instructions)) time,
    # O(1) space,
    # Approach: hashmap, simulation
    def isRobotBounded(self, instructions: str) -> bool:
        dist = defaultdict(int)
        rightOf = {
            "N" : "E", "E": "S", "S": "W", "W": "N"
        }
        leftOf = {
            "N": "W", "W": "S", "S": "E", "E": "N"
        }
        
        curr_direction = "N"
        
        for _ in range(4):
            for instruction in instructions:
                if instruction == "G":
                    dist[curr_direction] += 1
                elif instruction == "L":
                    curr_direction = leftOf[curr_direction]
                elif instruction == "R":
                    curr_direction = rightOf[curr_direction]
                
        return dist["N"] == dist["S"] and dist["E"] == dist["W"]