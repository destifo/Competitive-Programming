from typing import List


class TrieNode:
    
    def __init__(self, char):
        self.char = char
        self.end_of_word = False
        self.children = {}
        
    def getChild(self, char):
        return self.children.get(char, None)
    
    
    def addChild(self, char):
        if char in self.children:
            return
        
        self.children[char] = TrieNode(char)


class Trie:

    def __init__(self):
        self.root = TrieNode("")
        

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if not curr.getChild(ch):
                curr.addChild(ch)
            curr = curr.getChild(ch)
        
        curr.end_of_word = True
            

    def getRoot(self, word: str) -> bool:
        
        curr = self.root
        root = []
        for ch in word:
            curr = curr.getChild(ch)
            root.append(ch)
            if not curr:
                return word
            
            if curr.end_of_word:
                return "".join(root)
        
        return word


class Solution:
    
    # O(sum(words len in dictionary) + sum(words len in sentence))
    # O(sum(words len in dictionary)) space,
    # Approach: trie, 
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        
        ans = []
        for word in sentence.split():
            ans.append(trie.getRoot(word))
            
        return " ".join(ans)