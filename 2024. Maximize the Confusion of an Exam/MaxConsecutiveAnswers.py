class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: two pointers, 
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        k_copy = k
        
        longst_true = 0
        l, r = 0, 0
        
        while r < n:
            if answerKey[r] == 'T':
                r +=1
                continue
            
            if k_copy > 0:
                r +=1
                k_copy -=1
                continue
            
            longst_true = max(longst_true, r-l)
            while l < r and answerKey[l] == 'T':
                l +=1
                
            if l == r:  r +=1
            
            l +=1
            k_copy +=1
        
        longst_true = max(longst_true, r-l)
        
        longst_false = 0
        l, r = 0, 0
        while r < n:    
            if answerKey[r] == 'F':
                r +=1
                continue
            
            if k > 0:
                r +=1
                k -=1
                continue
            
            longst_false = max(longst_false, r-l)
            while l < r and answerKey[l] == 'F':
                l +=1
                
            if l == r:  r +=1
            
            l +=1
            k +=1
        
        longst_false = max(longst_false, r-l)
        
        return max(longst_true, longst_false)
    

    def findLongestConsecutive(self, answerKey: str, k: int, target: str) -> int:
        
        longest = 0
        left, right = 0, 0
        
        while right < len(answerKey):
            if answerKey[right] != target:
                if k > 0:
                    k -= 1
                else:
                    longest = max(longest, right-left)
                    while left < right and k == 0 and answerKey[left] == target:
                        left += 1  
                    left += 1
            right += 1
        
        longest = max(longest, right-left)
        return longest
                
    
    
    # O(n) time,
    # O(1) space,
    # Approach: sliding window, two pointers
    def maxConsecutiveAnswers2(self, answerKey: str, k: int) -> int:
        max_trues = self.findLongestConsecutive(answerKey, k, "T")
        max_falses = self.findLongestConsecutive(answerKey, k, "F")
        
        return max(max_trues, max_falses)