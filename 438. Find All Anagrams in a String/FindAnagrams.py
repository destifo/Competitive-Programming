from collections import Counter, defaultdict
from typing import List


class Solution:
    # O(n^2) time,
    # O(n) space,
    # Approach: two pointers, sliding window, hashmap
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def areEqual(d1, d2) -> bool:            
            for key, value in d1.items():
                if key not in d2.keys() or d2[key] != value:    return False
            
            return True
        
        
        window = {}
        p_set = Counter(p)
        n = len(p)
        m = len(s)
        if n > m:
            return []
        l, r = 0, n-1
        result = []
        
        for i in range(n-1):
            window[s[i]] = window.get(s[i], 0) + 1
        
        while r < m:
            window[s[r]] = window.get(s[r], 0) + 1
            if areEqual(p_set, window):
                result.append(l)
            window[s[l]] = window.get(s[l], 0) - 1
            l +=1
            r +=1
        
        return result

    
    def isAnagram(self, p_count, count2) -> bool:
        
        for ch, val in p_count.items():
            if count2[ch] != val:
                return False
            
        return True
    
    # O(len(p) + len(s)) time,
    # O(1) space,
    # Approach: hashmap, sliding window
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        
        if len(p) > len(s): return ans
        
        p_count = Counter(p)
        window = defaultdict(int)
        left, right = 0, len(p)
        
        for i in range(right):
            window[s[i]] += 1
            
        while right <= len(s):
            
            if self.isAnagram(p_count, window):
                ans.append(right-len(p))
            
            window[s[left]] -= 1
            if right < len(s):  window[s[right]] += 1
            left += 1
            right += 1
        
        return ans


sol = Solution()
print(sol.findAnagrams("cbaebabacd"
,"abc"))