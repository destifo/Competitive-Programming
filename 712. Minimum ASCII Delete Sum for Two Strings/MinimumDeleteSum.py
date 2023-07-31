class Solution:
    
    def findMinDeletedVal(self, i, j, word1, word2, ascii_prefix_sum1, ascii_prefix_sum2, memo) -> int:
        
        if i == len(word1):
            return ascii_prefix_sum2[-1]-ascii_prefix_sum2[j]
        
        if j == len(word2):
            return ascii_prefix_sum1[-1]-ascii_prefix_sum1[i]
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if word1[i] == word2[j]:
            return self.findMinDeletedVal(i+1, j+1, word1, word2, ascii_prefix_sum1, ascii_prefix_sum2, memo)
        
        delete_first = ord(word1[i]) + self.findMinDeletedVal(i+1, j, word1, word2, ascii_prefix_sum1, ascii_prefix_sum2, memo)
        delete_second = ord(word2[j]) + self.findMinDeletedVal(i, j+1, word1, word2, ascii_prefix_sum1, ascii_prefix_sum2, memo)
        
        memo[(i, j)] = min(delete_first, delete_second)
        return memo[(i, j)]
    
    
    # O(len(s1)*len(s2)) time,
    # O(len(s1)*len(s2)) space,
    # Approach: top down dp, memoization, string
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        ascii_prefix_sum1 = [0]
        ascii_prefix_sum2 = [0]
        
        tot = 0
        for ch in s1:
            tot += ord(ch)
            ascii_prefix_sum1.append(tot)
            
        tot = 0
        for ch in s2:
            tot += ord(ch)
            ascii_prefix_sum2.append(tot)
            
        return self.findMinDeletedVal(0, 0, s1, s2, ascii_prefix_sum1, ascii_prefix_sum2, {})
    
    
    
    # O(n^2) time,
    # O(n^2) space,
    # Approach: bottom up dp, string 
    def minimumDeleteSum2(self, s1: str, s2: str) -> int:
        dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

        for i in range(len(s1)-1, -1, -1):
            dp[i][-1] = dp[i+1][-1] + ord(s1[i])
            
        for j in range(len(s2)-1, -1, -1):
            dp[-1][j] = dp[-1][j+1] + ord(s2[j])

        for i in range(len(s1)-1, -1, -1):
            for j in range(len(s2)-1, -1, -1):
                dp[i][j] = min(dp[i+1][j]+ord(s1[i]), dp[i][j+1]+ord(s2[j]))
                if s1[i] == s2[j]:
                    dp[i][j] = min(dp[i][j], dp[i+1][j+1])
                    
        return dp[0][0]