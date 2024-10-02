'''
https://leetcode.com/problems/word-ladder-ii/
'''


from collections import deque
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        vstd = set()
        pattern_map = {}
        ans = []
        
        def buildPattern() -> None:
            addWordPattern(beginWord)
            for word in wordList:
                addWordPattern(word)
                
        
        def addWordPattern(word: str) -> None:
            patterns = getPatterns(word)
            
            for pattern in patterns:
                if pattern not in pattern_map.keys():
                    pattern_map[pattern] = []
                pattern_map[pattern].append(word)
        
        
        def getPatterns(word: str) -> List[str]:
            patterns = []
            for i in range(len(word)):
                pattern = word[:i] + '#' + word[i+1:]
                patterns.append(pattern)
                
            return patterns
        
        
        def getNeighbours(root_word: str) -> List[str]:
            neighbours = []
            patterns = getPatterns(root_word)
            
            for pattern in patterns:
                words = pattern_map[pattern]
                for word in words:
                    if word != root_word:
                        neighbours.append(word)
                
            return neighbours
        
        
        def findMinToEndword(root_word:str) -> int:
            qu = deque()
            qu.append(root_word)
            depth = 0
            
            while qu:
                n = len(qu)
                depth +=1
                for i in range(n):
                    root_word = qu.popleft()
                    if root_word in vstd:   continue
                    
                    if root_word == endWord:
                        return depth
                    
                    vstd.add(root_word)
                    neighbours = getNeighbours(root_word)
                    for nb in neighbours:
                        qu.append(nb)
                    
            return 0
        
        
        def dfs(root_word:str, length:int, max_depth:int, seq:List[str]) -> None:
            if length > max_depth:
                return
            
            # vstd.add(root_word)
            if root_word == endWord:
                ans.append(seq[::])
                return
            
            # seq.append(root_word)
            neighbours = getNeighbours(root_word)
            # if root_word == 'hot':
            #     print(neighbours)
            for nb in neighbours:
                # if nb in vstd:  continue
                seq.append(nb)
                dfs(nb, length+1, max_depth, seq)
                seq.pop()
            
            
            
        buildPattern()
        min_dep = findMinToEndword(beginWord)
        # vstd = set()
        dfs(beginWord, 1, min_dep, [beginWord])
        return ans