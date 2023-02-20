from collections import Counter
from typing import List


class Solution:
    
    def buildString(self, count) -> str:
        word = []
        
        for ch, cnt in count.items():
            if cnt > 0:
                for _ in range(cnt):
                    word.append(ch)
        
        word.sort()
        return "".join(word)
    
    
    def removeChars(self, count1, sticker_count) -> None:
        
        for ch, cnt in sticker_count.items():
            if ch not in count1:
                continue
            
            count1[ch] -= cnt
            if count1[ch] < 0:  count1.pop(ch)
                    
    
    def chooseSticker(self, char_count, stickers, memo):
        
        word = self.buildString(char_count)
        
        if len(word) <= 0:
            return 0
        
        if word in memo:
            return memo[word]
        
        min_stickers = float('inf')
        for sticker in stickers:
            first_char = word[0]
            if sticker[first_char] == 0:
                continue
            copied = char_count.copy()
            self.removeChars(copied, sticker)

            chosen_stickers = 1 + self.chooseSticker(copied, stickers, memo)
            min_stickers = min(min_stickers, chosen_stickers)
            
        memo[word] = min_stickers
        return min_stickers
    
    
    # O(len(stickers)*len(target)) time,
    # space complexity here is tricky,
    # Approach: dp top down, hashtables, 
    def minStickers(self, stickers: List[str], target: str) -> int:
        letters = set()
        for sticker in stickers:
            for ch in sticker:
                letters.add(ch)
                
        for ch in target:
            if ch not in letters:
                return -1
            
        stickers = [Counter(sticker) for sticker in stickers]
            
        return self.chooseSticker(Counter(target), stickers, {})