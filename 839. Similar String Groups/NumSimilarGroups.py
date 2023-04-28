from typing import List


class Solution:
    
    def find(self, node: int, parent: List[int]) -> int: 
        if node != parent[node]:
            parent[node] = self.find(parent[node], parent)
            
        return parent[node]
    
    
    def union(self, node1: int, node2: int, parent: List[int]) -> None:
        p1 = self.find(node1, parent)
        p2 = self.find(node2, parent)
        
        if p1 < p2:
            parent[p2] = p1
        else:
            parent[p1] = p2
    
    
    def areSimilarWords(self, word1: str, word2: str) -> bool:  
        dissimilar_indices = []
        
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                dissimilar_indices.append(i)
                
            if len(dissimilar_indices) > 2:
                return False
        
        if len(dissimilar_indices) == 0:
            return True
        
        if len(dissimilar_indices) == 1:
            return False
        
        i, j = dissimilar_indices
        return word1[i] == word2[j] and word1[j] == word2[i]
    
    
    # O(len(strs)^2 * len(str[i]))
    # O(len(strs)) space,
    # Approach: union find, string
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = [i for i in range(len(strs))]
        
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if self.areSimilarWords(strs[i], strs[j]):
                    self.union(i, j, parent)
        
        for i in range(len(strs)):
            parent[i] = self.find(i, parent)
        
        return len(set(parent))