class Solution:
    
    def findMinDist(self, i, j, word1, word2, memo) -> int:
        
        if j == len(word2):
            return len(word1)-i
        
        if i == len(word1):
            return len(word2)-j
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if word1[i] == word2[j]:
            return self.findMinDist(i+1, j+1, word1, word2, memo)
        
        replace = 1 + self.findMinDist(i+1, j+1, word1, word2, memo)
        delete = 1 + self.findMinDist(i+1, j, word1, word2, memo)
        insert = 1 + self.findMinDist(i, j+1, word1, word2, memo)
        
        memo[(i, j)] = min(replace, delete, insert)
        return memo[(i, j)]
    
    
    # O(len(word1)*len(word2)) time,
    # O(len(word1)*len(word2)) space,
    # Approach: top down dp, memoization, string
    def minDistance(self, word1: str, word2: str) -> int:
        return self.findMinDist(0, 0, word1, word2, {})
        
        '''
        
        ros
        
        last
        plas
        
        mexe
        exec
        
        exec
        eexec
        
        if equal => dfs(i+1, j+1) 
        if j == n => return m-i
        if replace => 1 + dfs(i+1, j+1)
        if n-j >= m-i and delete => 1 + dfs(i+1, j)
        if n <= m and add => 1 + dfs(i, j+1)
        
        '''