from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: string, array 
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
            
        return letters[0]