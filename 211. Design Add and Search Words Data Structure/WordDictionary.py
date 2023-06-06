'''
https://leetcode.com/problems/design-add-and-search-words-data-structure/
'''


from typing import List


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
        
    def getChildren(self) -> List:
        return self.children.keys()
        
    def getChild(self, char):
        return self.children[char]
        

class WordDictionary:

    def __init__(self):
        self.root = Node(' ')
        self.searchResult = {}

    # O(l) time, l --> length of the word
    # O(l) space, 
    def addWord(self, word: str) -> None:
        self.searchResult = {}
        curr = self.root
        for ch in word:
            if not curr.hasChild(ch):
                curr.addChild(ch)
            curr = curr.getChild(ch)
            
        curr.isEndOfWord = True
        
    # O(l) time,
    # O(n) space, n --> number of words searched 
    def search(self, word: str) -> bool:
        if word not in self.searchResult.keys():
            self.searchResult[word] = self.__search(self.root, word) 
        return self.searchResult[word]
    
    
    def __search(self, root, word) -> bool:
        curr = root
        for index, ch in enumerate(word):
            if not curr.hasChild(ch) and ch != '.':
                return False
            if ch == '.':
                for child in curr.getChildren():
                    # print(word[index+1:])
                    isWordFound = self.__search(curr.getChild(child), word[index+1:])
                    if isWordFound: return True
                return False
            else:
                curr = curr.getChild(ch)
            
        return curr.isEndOfWord
        


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('at')
obj.addWord('and')
obj.addWord('an')
obj.addWord('add')
print(obj.search('a'))
print(obj.search('.at'))
obj.addWord('bat')
print(obj.search('.at'))
# print(obj.search('bad'))
# print(obj.search('mad'))
# print(obj.search('.ad'))
# print(obj.search('b..'))