class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: counting, 
    def halvesAreAlike(self, s: str) -> bool:
        vowels = { 'a', 'e', 'i', 'o', 'u' }
        count = 0
        
        for i, ch in enumerate(s):
            if ch.lower() in vowels:
                if i < (len(s)//2):
                    count += 1
                else:
                    count -= 1

        return count == 0