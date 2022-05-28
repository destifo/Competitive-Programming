'''
https://leetcode.com/problems/minimum-moves-to-reach-target-score/
'''


class Solution:
    def minMoves(self, target: int, maxDoubles: int):
        curr = target
        count = 0
        
        while curr != 1:
            if maxDoubles > 0 and curr % 2 == 0:
                maxDoubles -=1
                curr //=2
            else:
                if maxDoubles > 0:
                    curr -=1
                else:
                    count += curr - 1
                    return count
                
            count +=1
            
        return count