from functools import reduce
import math
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        buffer, buffer_len, result = [], 0, []
        
        for word in words:
            if len(word) + buffer_len + len(buffer) - 1 >= maxWidth:
                free_spaces = maxWidth - buffer_len
                count_spaces = len(buffer) - 1
                
                for i in range(len(buffer)):
                    w = buffer[i]
                    
                    space2word = free_spaces if count_spaces == 0 else math.ceil(free_spaces/count_spaces)
                    
                    buffer[i] = buffer[i] + ''.join([' '] * space2word)
                    
                    free_spaces -= space2word
                    count_spaces -= 1
                    
                result.append(''.join(buffer))
                buffer, buffer_len = [], 0
                
            buffer.append(word)
            buffer_len += len(word)
            
        buffer = ' '.join(buffer)
        
        if len(buffer) < maxWidth:
            buffer = buffer + ''.join([' '] * (maxWidth - len(buffer)))
        
        result.append(buffer)
        
        return result 
    
    
    def justifyText(self, index: int, rem: int, maxWidth: int, curr_words: List[str], words: List[str]) -> None:
        
        if index == len(words):
            self.justified.append(curr_words)
            return
        
        word = words[index]
        if rem >= len(word):
            rem -= len(word)+1
            curr_words.append(word)
        else:
            rem = maxWidth-len(word)-1
            self.justified.append(curr_words)
            curr_words = [word]
        self.justifyText(index+1, rem, maxWidth, curr_words, words)
    
    
    # O(len(words)*len(word)) time,
    # O(len(words)*len(word)) space,
    # Approach: simulation, array, greedy, 
    def fullJustify2(self, words: List[str], maxWidth: int) -> List[str]:
        self.justified = []
        self.justifyText(0, maxWidth, maxWidth, [], words)
        
        ans = []
        for i, words in enumerate(self.justified):
            curr = ""
            rem_space = maxWidth-reduce(lambda x, y:x + len(y), words, 0)
            gap = rem_space//(len(words)-1) if len(words) > 1 else maxWidth-len(words[0])
            rem_gap = rem_space % (len(words)-1) if len(words) > 1 else 0
            if i == len(self.justified)-1:
                curr = " ".join(words)
                curr += " "*(maxWidth-len(curr))
                ans.append(curr)
                break
            for word in words:
                curr += word
                curr += " "*gap
                if rem_gap:
                    curr += " "
                    rem_gap -= 1
            if len(words) > 1:
                curr = curr.rstrip()
            ans.append(curr)
                    
        return ans