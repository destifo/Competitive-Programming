'''
https://leetcode.com/problems/divisor-game/
'''


class Solution:
    # O(1) time,
    # O(1) space,
    # Approach: math, 
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0