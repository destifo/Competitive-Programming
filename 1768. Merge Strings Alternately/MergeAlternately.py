class Solution:
    
    # O(max(m, n)) time,
    # O(m + n) space,
    # Apporach: string, simulation
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        
        i = 0
        while i < min(len(word1), len(word2)):
            ans.append(word1[i])
            ans.append(word2[i])
            i += 1
            
        while i < len(word1):
            ans.append(word1[i])
            i += 1
            
        while i < len(word2):
            ans.append(word2[i])
            i += 1
            
        return "".join(ans)