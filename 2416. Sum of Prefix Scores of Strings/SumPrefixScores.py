from typing import List


class TrieNode:
    
    def __init__(self, ch: str) -> None:
        self.ch = ch
        self.endOfWord = 0
        self.vstd = 0
        self.children = {}


class Solution:
    # O(n*m) time, n --> len(words), m --> len(words[i]) 
    # O(n*m) space,
    # Approach: trie, hashtable
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = TrieNode('')
        ans = []        
        
        def addWord(word: str) -> None:
            curr = trie
            for c in word:
                if c not in curr.children:
                    nod = TrieNode(c)
                    curr.children[c] = nod
                curr = curr.children[c]
                curr.vstd +=1
                
            curr.endOfWord +=1 
            
        
        def calcScore(word: str) -> int:
            score = 0
            curr = trie
            
            for c in word:
                curr = curr.children[c]
                score += curr.vstd
            return score
        
        
        for word in words:
            addWord(word)
            
        for word in words:
            score = calcScore(word)
            ans.append(score)
        
        return ans