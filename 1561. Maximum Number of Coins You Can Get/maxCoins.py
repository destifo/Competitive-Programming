'''
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/submissions/
'''

class Solution:
    #looks like today is my lucky day, worked the first time :)
    def maxCoins(self, piles) -> int:
        piles.sort()
        pile_len = len(piles)

        tot_coins = 0

        for i in range(-2, (((pile_len//3)*2) * -1) - 1, -2):
            tot_coins += piles[i]

        return tot_coins



sol = Solution()

print(sol.maxCoins([9,8,7,6,5,1,2,3,4]))