from collections import Counter
from typing import Dict, List


class Solution:
    
    def canTake(self, count, letter_count) -> int:
        
        for ch, cnt in count.items():
            if ch not in letter_count or letter_count[ch] < cnt:
                return False
            
        return True
    
    
    def reduce(self, count, letter_count) -> None:
        
        for ch, cnt in count.items():
            letter_count[ch] -= cnt
    
    
    def addCount(self, count, letter_count) -> None:
        
        for ch, cnt in count.items():
            letter_count[ch] += cnt
            
            
    def getMapStr(self, count: Dict[str, int]) -> str:
        
        str_build = []
        for ch, cnt in count.items():
            str_build.append(f"{ch}{cnt}")
            
        return "".join(str_build)
            
    
    def getMaxScore(self, index: int, words, letter_count: Dict[str, int], memo) -> int:
        
        if index == len(words):
            return 0
        
        state = (index, self.getMapStr(letter_count))
        if state in memo:
            return memo[state]
        
        score, count = words[index]
        maxx = 0
        if self.canTake(count, letter_count):
            self.reduce(count, letter_count)
            maxx = max(maxx, score + self.getMaxScore(index+1, words, letter_count, memo))
            self.addCount(count, letter_count)
            
        maxx = max(maxx, self.getMaxScore(index+1, words, letter_count, memo))
        memo[state] = maxx
        
        return maxx
    
    
    def getScore(self, word: str, scores: List[int]) -> int:
        
        score = 0
        for ch in word:
            score += scores[ord(ch)-97]
            
        return score
    
    
    # O(nlogn) time, n --> len(words)
    # O(n) space,
    # Approach: sorting, hash map, memoization
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        word_meta = []
        for word in words:
            word_meta.append((self.getScore(word, score), Counter(word)))
        letter_count = Counter(letters)
        word_meta.sort(reverse=True)
        
        return self.getMaxScore(0, word_meta, letter_count, {})