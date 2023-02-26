class Solution:
    
    def findMinDist(self, i, j, word1, word2, memo):
        
        if i == len(word1):
            return len(word2)-j
        
        if j == len(word2):
            return len(word1)-i
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if word1[i] == word2[j]:
            return self.findMinDist(i+1, j+1, word1, word2, memo)
        
        delete_first = 1 + self.findMinDist(i+1, j, word1, word2, memo)
        delete_second = 1 + self.findMinDist(i, j+1, word1, word2, memo)
        
        memo[(i, j)] = min(delete_first, delete_second)
        return memo[(i, j)]
    
    
    # O(len(word1)*len(word2)) time,
    # O(len(word1)*len(word2)) space,
    # Approach: top down dp, memoization, string
    def minDistance(self, word1: str, word2: str) -> int:
        return self.findMinDist(0, 0, word1, word2, {})