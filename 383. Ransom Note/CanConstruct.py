'''
https://leetcode.com/problems/ransom-note/
'''


from collections import Counter


class Solution:
    # O(n) time, 
    # O(n) space,
    # Approach: hashtable,
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rNote_count = Counter(ransomNote)
        magz_count = Counter(magazine)
        
        for ch, count in rNote_count.items():
            if ch not in magz_count.keys() or magz_count[ch] < count:
                    return False
                
        return True