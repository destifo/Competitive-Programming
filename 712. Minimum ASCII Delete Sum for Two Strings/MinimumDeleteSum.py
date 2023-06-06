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