'''
https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
'''

class Solution:
    # I found the hints to be more than helpful
    def getDescentPeriods(self, prices):
        n = len(prices)
        ans = n
        if n == 1:
            return ans

        l, r = 0, 1
        while r < n:
            curr = 1
            while r < n and prices[l] - prices[r] == 1:
                curr +=1
                r +=1
                l +=1
            period = (curr * (curr - 1))//2
            ans +=period
            r +=1
            l +=1

        return ans

sol = Solution()
print(sol.getDescentPeriods([4,3,2,1,4]))            