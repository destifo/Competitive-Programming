from collections import defaultdict
from typing import List


class TrieNode:
    
    def __init__(self, char: str) -> None:
        self.char = char
        self.children = {}
        self.endOfWord = False

class Trie:
    
    def __init__(self) -> None:
        self.root = TrieNode(" ")
        
    def addWord(self, word: str) -> None:
        
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode(ch)
            curr = curr.children[ch]
            
        curr.endOfWord = True
        
        
    def getAllWords(self, node: TrieNode, path: List[str], keys: List[str]):
        if node.endOfWord:
            word = "".join(path)
            keys.append(word)
            
        for ch in node.children.keys():
            path.append(ch)
            self.getAllWords(node.children[ch], path, keys)
            path.pop()
        
    
    def getKeysWithPrefix(self, prefix: str) -> None:
        word = []
        curr = self.root
        keys = []
        
        for ch in prefix:
            if ch not in curr.children:
                return []
            word.append(ch)
            curr = curr.children[ch]
            
        self.getAllWords(curr, word, keys)
        return keys



class MapSum:

    def __init__(self):
        self._map = defaultdict(int)
        self.trie = Trie()
        

    def insert(self, key: str, val: int) -> None:
        self._map[key] = val
        self.trie.addWord(key)
        

    def sum(self, prefix: str) -> int:
        keys = self.trie.getKeysWithPrefix(prefix)
        total = 0
        for key in keys:
            total += self._map[key]
            
        return total


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)