'''
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
'''


from collections import Counter, defaultdict
from typing import Dict


class Solution:
    # O(n-k) time,
    # O(1) space,
    # Approach: sliding window, two pointers, hashtable, 
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, k
        count = Counter(s[l:r])
        
        def countVowels(count) -> int:
            vowels = ['a', 'e', 'i', 'o', 'u']
            tot = 0
            
            for vowel in vowels:
                tot += count.get(vowel, 0)
                
            return tot
        
        max_count = countVowels(count)
        
        while r < n:
            count[s[l]] -=1
            count[s[r]] = count.get(s[r], 0) + 1
            
            max_count = max(max_count, countVowels(count))
            if max_count == k:
                return max_count
            
            l +=1
            r +=1
            
        return max_count
    

    def countVowels(self, window: Dict[str, int]) -> int:
        
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        for vowel in vowels:
            count += window[vowel]
            
        return count
    
    
    # O(n) time,
    # O(1) space,
    # Approach: sliding window, two pointers, hash table
    def maxVowels2(self, s: str, k: int) -> int:
        window = defaultdict(int)
        left, right = 0, k
        
        for i in range(k):
            window[s[i]] += 1
            
        ans = self.countVowels(window)
        while right < len(s):
            if ans == k: # pruning
                break
            
            window[s[left]] -= 1
            left += 1
            window[s[right]] += 1
            right += 1
            ans = max(ans, self.countVowels(window))
            
        return ans