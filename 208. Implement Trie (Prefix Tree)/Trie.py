'''
https://leetcode.com/problems/implement-trie-prefix-tree/
'''


class Node:
    value: str
    isEndOfWord: bool
    children: map
        
    def __init__(self, value:str) -> None:
        self.value = value
        self.isEndOfWord = False
        self.children = {}
        
    def hasChild(self, char) -> bool:
        return char in self.children.keys()
    
    def addChild(self, char) -> None:
        self.children[char] = Node(char)
        
    def getChild(self, char):
        return self.children[char]


class Trie:
    root: Node

    def __init__(self):
        self.root = Node('')

    # O(L) time, 
    def insert(self, word: str) -> None:
        curr = self.root
        
        for ch in word:
            if not curr.hasChild(ch):
                curr.addChild(ch)
            curr = curr.getChild(ch)
            
        curr.isEndOfWord = True
        
    # O(L) time,
    # O(1) space
    def search(self, word: str) -> bool:
        curr = self.root
        
        for ch in word:
            if not curr.hasChild(ch):
                return False
            curr = curr.getChild(ch)
            
        if not curr.isEndOfWord:   return False
        
        return True
        
    # O(L) time,
    # O(1) space
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for ch in prefix:
            if not curr.hasChild(ch):
                return False
            curr = curr.getChild(ch)
            
        return True



class TrieNode:
    
    def __init__(self, ch: str) -> None:
        self.children = {}
        self.ends = 0
        self.ch = ch
        

class Trie3:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode(ch)
            curr = curr.children[ch]
        curr.ends += 1
        

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
            
        return curr.ends > 0
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)