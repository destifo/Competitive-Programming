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
            

    def search(self, word: str) -> bool:
        
        curr = self.root
        for ch in word:
            curr = curr.getChild(ch)
            if not curr:
                return False
        
        return curr.end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            curr = curr.getChild(ch)
            if not curr:
                return False
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)