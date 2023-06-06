'''
https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
'''


from collections import Counter


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: sliding window, hashmap, two pointers
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        
        l, r = 0, k
        window = Counter(blocks[l:r])
        # print(window)
        min_ops = window['W']
        
        while r < n:
            window[blocks[l]] -=1
            window[blocks[r]] +=1
            
            whites = window['W']
            if whites == 0:
                return 0
            
            min_ops = min(min_ops, whites)
            l +=1
            r +=1
            
        return min_ops