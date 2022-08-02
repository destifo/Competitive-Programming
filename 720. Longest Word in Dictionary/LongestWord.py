'''
https://leetcode.com/problems/longest-word-in-dictionary/
'''


from typing import List, Optional


class TrieNode:
    value: str
    isEndOfWord: bool
    children: map[str:Optional[TrieNode]]
        
    def __init__(self, value:str) -> None:
        self.value = value
        self.isEndOfWord = False
        self.children = {}
        
    def hasChild(self, char) -> bool:
        return char in self.children.keys()
    
    def addChild(self, char) -> None:
        self.children[char] = TrieNode(char)
        
    def getChildren(self) -> List[str]:
        return self.children.keys()
        
    def getChild(self, char):
        return self.children[char]

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode(' ')
        ans = [''] * 1
        
        # build the trie
        for word in words:
            curr = root
            for ch in word:
                if not curr.hasChild(ch):
                    curr.addChild(ch)
                curr = curr.getChild(ch)
            curr.isEndOfWord = True
                
        def dfs(root:Optional[TrieNode], word) -> None:
            # print('hey')
            if root.isEndOfWord:
                possible_word = (word + root.value)
                if len(ans) == 0 or len(possible_word) >= len(ans[0]):
                    addWord(possible_word)
                for child in root.getChildren():
                    dfs(root.getChild(child), possible_word)
            else:
                return
                    
                    
        
        def addWord(word:str) -> None:
            n = len(word)
            m = len(ans[0])
            if n > m or ans[0] > word:
                ans[0] = word
          
        for child in root.getChildren():
            dfs(root.getChild(child), '')
            
        return ans[0]