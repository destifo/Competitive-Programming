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