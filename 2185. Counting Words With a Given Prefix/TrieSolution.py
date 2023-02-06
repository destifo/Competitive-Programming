from typing import List


class Trie:
    
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.endOfWord = 0
        
    def getChild(self, char):
        if char in self.children:
            return self.children[char]
        
        return None
    
    
    def addChild(self, char) -> None:
        if char not in self.children:
            self.children[char] = Trie(char)


class Solution:
    
    def countPrefixes(self, trie) -> int:
        
        count = trie.endOfWord
        for child in trie.children.values():
            count += self.countPrefixes(child)
            
        return count
    
    
    # O(len(word) + len(pref)) time,
    # O((sum(words))) space,
    # Approach: string, 
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefixes = 0
        
        # add words to Trie
        trie = Trie(" ")
        for word in words:
            curr = trie
            for char in word:
                curr.addChild(char)
                curr = curr.getChild(char)
                
            curr.endOfWord += 1
        
        # count words with that prefix
        curr = trie
        for char in pref:
            curr = curr.getChild(char)
            if not curr:    return prefixes
            
        prefixes = self.countPrefixes(curr)
        
        return prefixes