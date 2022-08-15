class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: hashtable, 
    def romanToInt(self, s: str) -> int:
        char_map = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        
        n = len(s)
        num = 0
        skip_next = False
        for i, ch in enumerate(s):
            if skip_next:
                skip_next = False
                continue
            
            if ch == 'I' and (i+1 < n and (s[i+1] == 'V' or s[i+1] == 'X')):
                val = char_map[s[i+1]] - char_map[ch]
                num +=val
                skip_next = True
                continue
            if ch == 'X' and (i+1 < n and (s[i+1] == 'L' or s[i+1] == 'C')):
                val = char_map[s[i+1]] - char_map[ch]
                num +=val
                skip_next = True
                continue
            if ch == 'C' and (i+1 < n and (s[i+1] == 'D' or s[i+1] == 'M')):
                val = char_map[s[i+1]] - char_map[ch]
                num +=val
                skip_next = True
                continue
            num += char_map[ch]
            
        return num