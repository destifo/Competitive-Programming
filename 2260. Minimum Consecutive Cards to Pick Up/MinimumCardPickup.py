'''
https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/
'''

from typing import SupportsAbs


class Solution:
    def minimumCardPickup(self, cards: list[int]):
        n = len(cards)
        if n == 1:  return -1
        subarray = set()
        subarray.add(cards[0])
        l, r = 0, 1
        min_cards = float('inf')

        while r < n:
            card = cards[r]
            if card in subarray:
                while card in subarray:
                    subarray.remove(cards[l])
                    l +=1
                min_cards = min(min_cards, r - l + 2)
                
            subarray.add(card)
            r +=1

        return -1 if min_cards == float('inf') else min_cards


sol = Solution()
print(sol.minimumCardPickup([95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6]))