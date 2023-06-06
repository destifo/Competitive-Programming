'''
https://leetcode.com/problems/permutation-in-string/
'''


from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1_count = Counter(s1)
        l, r = 0, n-1
        while r < len(s2):
            if s1_count == Counter(s2[l:r+1]):
                return True
            l +=1
            r +=1 
        return False

    
    def isPermutation(self, window, cnt1) -> bool:
        for ch, cnt in cnt1.items():
            if window[ch] != cnt:
                return False
            
        return True
    
    # O(len(s1)+len(s2)) time,
    # O(1) space,
    # Approach: sliding window, hashmap, 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window = defaultdict(int)
        left, right = 0, len(s1)
        
        for i in range(right):
            window[s2[i]] += 1
        
        while right < len(s2):
            if self.isPermutation(window, s1_count):
                return True
            window[s2[right]] += 1
            right += 1
            window[s2[left]] -= 1
            left += 1
        
        if self.isPermutation(window, s1_count):
            return True
                
        return False


sol = Solution()
print(sol.checkInclusion('ab', 'beac'))