class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: hashtable, 
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping1 = {}
        mapping2 = {}
        
        for i in range(len(s)):
            ch1, ch2 = s[i], t[i]
            if ch1 in mapping1 and mapping1[ch1] is not ch2 or ch2 in mapping2 and mapping2[ch2] is not ch1:
                return False
            else:
                mapping1[ch1] = ch2
                mapping2[ch2] = ch1
                
        return True