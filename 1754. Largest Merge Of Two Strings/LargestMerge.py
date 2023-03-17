class Solution:
    
    def isFirstLarger(self, i, j, word1, word2):
        return word1[i:] > word2[j:]
    
    
    # O(n^2) time,
    # O(n^2) space,
    # Approach: greedy, two pointers, 
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        
        merge = []
        while i < len(word1) and j < len(word2):
            if word1[i] > word2[j]:
                merge.append(word1[i])
                i += 1
            elif word2[j] > word1[i]:
                merge.append(word2[j])
                j += 1
            else:
                if self.isFirstLarger(i, j, word1, word2):
                    merge.append(word1[i])
                    i += 1
                else:
                    merge.append(word2[j])
                    j += 1
                
                
        while i < len(word1):
            merge.append(word1[i])
            i += 1
        
        while j < len(word2):
            merge.append(word2[j])
            j += 1
            
        return "".join(merge)