'''
https://leetcode.com/problems/longest-palindrome/
'''


from collections import Counter


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: hashmap,
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        
        isThereOdd = False
        even_count = 0
        
        for value in char_count.values():
            if value % 2 == 0:
                even_count += value
            else:
                if not isThereOdd:
                    isThereOdd = True
                even_count += (value-1)
                    
        longest_palnd = even_count
        longest_palnd += 1 if isThereOdd else 0
        
        return longest_palnd