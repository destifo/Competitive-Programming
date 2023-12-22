from collections import Counter


class Solution:
    
    
    # O(n) time,
    # O(1) space,
    # Approach: counting, prefix sum
    def maxScore(self, s: str) -> int:
        ones = Counter(s)['1']
        zeros = 0
        
        ans = 0
        for i in range(len(s)-1):
            ch = s[i]
            if ch == "0":
                zeros += 1
            else:
                ones -= 1
            
            score = zeros+ones
            ans = max(ans, score)
            if ans == len(s):
                break
            
        return ans