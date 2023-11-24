'''
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/submissions/
'''

from typing import List


class Solution:
    #looks like today is my lucky day, worked the first time :)
    def maxCoins(self, piles) -> int:
        piles.sort()
        pile_len = len(piles)

        tot_coins = 0

        for i in range(-2, (((pile_len//3)*2) * -1) - 1, -2):
            tot_coins += piles[i]

        return tot_coins
    
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: greedy, sorting
    def maxCoinsw(self, piles: List[int]) -> int:
        '''
        
        1, 2, 2, 2, 4, 7, 8, 9, 9
        
        s1 = 7 + 9 + 2 = 18
        s2 = 9 + 4 + 2 = 15
        
        find n,
        start from n and take the second highest sum in the left 2n piles
        '''
        
        n = len(piles)//3
        ans = 0
        
        piles.sort()
        for i in range(n, len(piles), 2):
            ans += piles[i]
            
        return ans



sol = Solution()

print(sol.maxCoins([9,8,7,6,5,1,2,3,4]))