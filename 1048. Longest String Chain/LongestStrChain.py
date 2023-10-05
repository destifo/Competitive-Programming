from typing import List


class Solution:
    
    def isSuccessor(self, succ: str, pred: str) -> bool:
        if pred == "":
            return True
        
        if len(pred) != len(succ) - 1:
            return False
        
        i, j = 0, 0
        have_pass = True
        while i < len(pred):
            if pred[i] == succ[j]:
                i += 1
            elif have_pass:
                have_pass = False
            else:
                return False
            j += 1
            
        return True
    
    
    def chooseWords(self, index: int, prev: str, words: List[str], memo) -> int:
        
        if index == len(words):
            return 0
        
        state = (index, prev)
        if state in memo:
            return memo[state]
        
        take = float('-inf')
        if self.isSuccessor(words[index], prev):
            take = 1 + self.chooseWords(index+1, words[index], words, memo)
            
        skip = self.chooseWords(index+1, prev, words, memo)
        
        memo[state] = max(take, skip)
        return memo[state]
    
    
    # O(n^2) time,
    # O(n^2) space,
    # Approach: dp, string, 
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        
        return max(self.chooseWords(0, "", words, {}), 1)