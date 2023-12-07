from typing import List


class Solution:
    
    def buildSentences(self, index: int, curr: List[str], dp: List[List[str]], ans: List[str]) -> None:
        
        if index >= len(dp)-1:
            ans.append(" ".join(curr))
            return

        for word in dp[index]:
            curr.append(word)
            self.buildSentences(index+len(word), curr, dp, ans)
            curr.pop()
    
    
    # O(n^2*m) time, n --> len(s), m --> len(wordDict)
    # O(n^2) space,
    # Approach: bottom up dp, dfs, backtracking 
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        dp = [[] for _ in range(len(s)+1)]
        dp[-1].append("")

        for i in range(len(s)-1, -1, -1):
            size = len(s)-i
            for word in wordDict:
                if size >= len(word):
                    if word == s[i:i+len(word)] and len(dp[i+len(word)]) > 0:
                        dp[i].append(word)
        
        self.buildSentences(0, [], dp, ans)

        return ans