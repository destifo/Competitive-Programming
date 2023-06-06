'''
https://leetcode.com/problems/unique-morse-code-words/
'''


from typing import List


class Solution:
    # O(len(words) * m) time, m --> the longest word in words
    # O(len(words)) space,
    # Apporach: hashtable,
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()
        
        def convertToMorse(word:str) -> str:
            morse_version = ''
            a_ascii_val = 97
            
            for ch in word:
                morse_version += morse_code[ord(ch)-a_ascii_val]
                
            return morse_version
        
        for word in words:
            transformations.add(convertToMorse(word))
            
        return len(transformations)