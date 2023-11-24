from collections import defaultdict


class Solution:
    
    # O(n^2/2) time,
    # O(n) space,
    # Approach: hashmap, 
    def countPalindromicSubsequence(self, s: str) -> int:
        '''
        
        first, iterate and as you go capture the index of the numbers,
        second, whenever u traverse a char, check if it has a prev occuring, and add the diff between the indices for the answer
        
        finally, return the answer
        
        '''
        
        prev_occ = {}
        pal_middle = defaultdict(set)
        ans = 0
        count = defaultdict(int)
        
        for i, ch in enumerate(s):
            if ch in prev_occ:
                for j in range(prev_occ[ch]+1, i):
                    if s[j] not in pal_middle[ch]:
                        ans += 1
                        pal_middle[ch].add(s[j])
                    
            prev_occ[ch] = i
            count[ch] += 1
            if count[ch] == 3:
                ans += 1
                count[ch] += 1
                
        return ans
    
    
    # O(n) time,
    # O(1) space,
    # Approach: hashmap, 
    def countPalindromicSubsequence2(self, s: str) -> int:
        
        ans = 0
        alphabets = 26
        
        for i in range(alphabets):
            ch = chr(i+97)
            left, right = s.find(ch), s.rfind(ch)
            chars = set()
            
            for i in range(left+1, right):
                chars.add(s[i])
            ans += len(chars)    
                
        return ans