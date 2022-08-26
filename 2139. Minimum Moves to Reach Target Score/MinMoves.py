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


    # O(maxDoubles) time,
    # O(1) space,
    # Approach: Greedy, Reverse thinking
    def minMoves2(self, target: int, maxDoubles: int) -> int:
        moves = 0
        
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                maxDoubles -=1
                target //=2
                moves +=1
            else:
                target -=1
                moves +=1
                
        if target > 1:
            moves += (target-1)
        
        return moves