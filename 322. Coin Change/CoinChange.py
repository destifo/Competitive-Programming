class Solution:
    # naive solution, TLE
    def coinChange(self, coins, amount: int):
        n = len(coins)
        memo = {}
        coins.sort()

        def dfs(i, rem, score):
            if i < 0 or rem < 0:
                return float('inf')

            if rem == 0:
                return score
            
            rem_score = (rem - coins[i], score + 1)
            if not memo.get((i, rem_score), None):
                memo[(i, rem - coins[i])] = dfs(i, rem - coins[i], score + 1)
            rem_score = (rem, score)
            if not memo.get((i - 1, rem_score), None):
                memo[(i - 1, rem)] = dfs(i - 1, rem, score)

            return min(memo[(i, rem - coins[i])], memo[(i - 1, rem)])

        ans = dfs(n - 1, amount, 0)
        return ans if ans != float('inf') else -1


    def coinChange(self, coins, amount: int):
        # opt solution, from neetcode
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for num in range(1, amount + 1):
            for coin in coins:
                if num - coin >= 0:
                    dp[num] = min(dp[num], 1+dp[num - coin])

        return dp[num] if dp[num] != float('inf') else -1