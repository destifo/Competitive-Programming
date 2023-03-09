from collections import defaultdict


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: hashtable, counting
    def getHint(self, secret: str, guess: str) -> str:
        bulls = set()
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls.add(i)
                
        non_bulls = defaultdict(int)
        for i in range(len(secret)):
            if i in bulls:
                continue
                
            non_bulls[secret[i]] += 1
        
        cows = 0
        for i in range(len(guess)):
            if i in bulls:
                continue
                
            cows += max(0, min(1, non_bulls[guess[i]]))
            non_bulls[guess[i]] -= 1
            
        return f"{len(bulls)}A{cows}B"