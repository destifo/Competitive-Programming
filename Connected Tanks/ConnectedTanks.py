
# Problem statement
'''
I took an interview test yesterday. I only passed half test cases. It is interesting, so I want to share it.
There are some tanks with different capabilities, they are connected. If the tank is full, it overflows into the next tank, one way. And each tank have a water pip for getting water at the same time. It needs we return the time the last tanks is full, and all tanks are full.
Test case 1: 
input
4 1 
30 
3 
7 
20
output 
10 30
Explanation:
There are 4 tanks, and the water per second is 1.
The capacity of the first tank is 30, and so on.
After 10 second the last tank will be full, and after 30 second all tanks are full.
Test case 2:
2 2 
4 
6
output
2 2
'''

import math
from typing import List, Tuple


class Solution:
    def findTime(self, tanks: List[int], speed: int) -> Tuple[int]:
        n = len(tanks)
        max_time = (tanks[0]/speed)
        if n == 1:  return max_time, max_time
        last_time = None
        stack = [[max_time, speed]]

        for i in range(1, n):
            tank = tanks[i]
            normal_time = tank/speed
            if normal_time < stack[-1][0]:
                # consider if stack[-1][1](prev_time) < time
                max_time = max(max_time, normal_time)
                stack.append([normal_time, speed])
                last_time = normal_time
            elif normal_time == stack[-1][0]:
                last_time = normal_time
                stack[-1][1] += speed
            elif normal_time > stack[-1][0]:
                prev = stack.pop()
                time = prev[0]
                left_vol = tank - (time*speed)
                curr_speed = prev[1] + speed
                if not stack:
                    opt_time = left_vol/curr_speed
                    time += opt_time
                    last_time = time
                while stack:
                    opt_time = left_vol/curr_speed

                    if stack[-1][0] < opt_time+time:
                        prev = stack.pop()
                        vol = curr_speed * (prev[0]-time)
                        time = prev[0]
                        left_vol -= vol
                        curr_speed += prev[1]
                    else:
                        time += opt_time
                        last_time = time
                        if stack[-1][0] == opt_time+time:
                            curr_speed += stack.pop()[1]
                        break
                
                max_time = max(max_time, time)
                stack.append([time, curr_speed])

        return last_time, max_time


sol = Solution()
tanks = [130,7,3,100]
speed = 1
print(sol.findTime(tanks, speed))