from collections import deque


class Solution:

    
    def racecar(self, target: int) -> int:
        dq=deque([(0,0,1)])
        while dq:
            move,pos,speed=dq.popleft()
            if pos==target:
                return move
            dq.append((move+1,pos+speed,speed*2))
            if (pos+speed>target and speed>0) or pos+speed<target and speed<0:
                speed=-1 if speed>0 else 1
                dq.append((move+1,pos,speed))
            else:
                continue