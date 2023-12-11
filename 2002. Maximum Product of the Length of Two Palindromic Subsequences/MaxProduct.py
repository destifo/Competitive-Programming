from typing import List, Set


class Solution:
    
    def isPali(self, chars: List[int]) -> bool:
        
        left, right = 0, len(chars)-1
        
        while left < right:
            if chars[left] != chars[right]:
                return False
            left += 1
            right -= 1
            
        return True
    
    
    def findPalis(self, index: int, indices: List[int], chars: List[str], s: str, cache: List[Set[int]]) -> None:
        
        if index == len(s):
            return
        
        indices.append(index)
        chars.append(s[index])
        if self.isPali(chars):
            cache.append(set(indices))
            
        self.findPalis(index+1, indices, chars, s, cache)
        indices.pop()
        chars.pop()
        self.findPalis(index+1, indices, chars, s, cache)
        
    
    def areDisjoint(self, s1: Set[int], s2: Set[int]) -> bool:
        
        for index in s1:
            if index in s2:
                return False
            
        return True
    
    
    # O(2^n*n) time,
    # O(2^n*n) space,
    # Approach: set, two pointers
    def maxProduct(self, s: str) -> int:
        cache = [] # List[set(pali_index)]
        
        self.findPalis(0, [], [], s, cache)
        
        ans = 0
        for i in range(len(cache)):
            for j in range(i+1, len(cache)):
                if self.areDisjoint(cache[i], cache[j]):
                    prod = len(cache[i])*len(cache[j])
                    ans = max(ans, prod)
                    
        return ans
    
    
    # O(2^n) time,
    # O(2^n) space,
    # Approach: bit masking,
    def maxProduct(self, s: str) -> int:
        n = len(s)
        palis = []
        
        # go over all the masks for all the subsequences
        for mask in range(1, 1 << n):
            chars = []
            
            # take the chars in the mask/subsequence
            for i in range(n):
                if mask & (1 << i) != 0:
                    chars.append(s[i])
            
            if self.isPali(chars):
                palis.append((mask, len(chars)))
                
        ans = 0
        for i in range(len(palis)):
            mask1, length1 = palis[i]
            for j in range(i+1, len(palis)):
                mask2, length2 = palis[j]
                prod = length1 * length2
                if mask1 & mask2 == 0 and prod > ans:
                    ans = prod
                    
        return ans