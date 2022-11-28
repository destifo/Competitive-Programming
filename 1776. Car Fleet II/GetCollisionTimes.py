from typing import List


class Solution:
    
    def collisionTime(self, cars, curr, next):
        
        return (cars[next][0] - cars[curr][0]) / (cars[curr][1]-cars[next][1])
    
    
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        
        stack = []
        
        collision_time = [-1.0 for _ in range(len(cars))]
        
        for i in range(len(cars)-1, -1, -1):
            
            while stack and ( cars[i][1] <= cars[stack[-1]][1] or (len(stack) > 1 and self.collisionTime(cars, i, stack[-1]) >= collision_time[stack[-1]]) ):
                stack.pop()
                             
            time = -1.0 if not stack else self.collisionTime(cars, i, stack[-1])
            collision_time[i] = time
            stack.append(i)
                             
        return collision_time                
                    
