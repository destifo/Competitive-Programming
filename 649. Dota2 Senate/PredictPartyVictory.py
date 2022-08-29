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
                