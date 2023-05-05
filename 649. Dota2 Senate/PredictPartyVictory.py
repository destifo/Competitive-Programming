'''
https://leetcode.com/problems/dota2-senate/
'''


from collections import Counter


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: greedy, hashset
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        count = Counter(senate)
        
        skip_r = 0
        skip_d = 0
        removed_r = set()
        removed_d = set()
        while count['D'] > 0 and count['R'] > 0:
            for i in range(n):
                s = senate[i]
                if s == 'R':
                    if skip_r <= 0 and i not in removed_r:
                        count['D'] -=1
                        skip_d +=1
                    else:
                        if i not in removed_r:
                            skip_r -=1
                            removed_r.add(i)
                else:
                    if skip_d <= 0 and i not in removed_d:
                        count['R'] -=1
                        skip_r +=1
                    else:
                        if i not in removed_d:
                            skip_d -=1
                            removed_d.add(i)
                        
        if count['D'] > 0:
            return 'Dire'
        else:
            return 'Radiant'
        

    # O(nlogn) time,
    # O(nlogn) space,
    # Approach: counting, greedy
    def predictPartyVictory(self, senate: str) -> str:
        skip_r, skip_d = 0, 0
        r_count, d_count = 0, 0
        next_state = []
        
        for senator in senate:
            if senator == "R":
                r_count += 1
            else:
                d_count += 1
        
        while d_count > 0 and r_count > 0:
            for senator in senate:
                if senator == "R":
                    if skip_r > 0:
                        skip_r -= 1
                        r_count -= 1
                    else:
                        next_state.append("R")
                        skip_d += 1
                else:
                    if skip_d > 0:
                        skip_d -= 1
                        d_count -= 1
                    else:
                        next_state.append("D")
                        skip_r += 1
                        
            senate = next_state
            next_state = []
            
        return "Radiant" if r_count > 0 else "Dire"
                