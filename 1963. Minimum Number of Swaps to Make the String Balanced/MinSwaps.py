class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: greedy, counting
    def minSwaps(self, s: str) -> int:
        right_op = len(s)-1
        while s[right_op] != '[':
            right_op -= 1
        
        s = list(s)
        swaps = 0
        diff = 0
        for i in range(len(s)):
            if s[i] == ']':
                diff -= 1
            else:
                diff += 1
                
            if diff < 0:
                s[i], s[right_op] = s[right_op], s[i]
                right_op -= 1
                while s[right_op] != '[':
                    right_op -= 1
                swaps += 1
                diff += 2
                
        return swaps