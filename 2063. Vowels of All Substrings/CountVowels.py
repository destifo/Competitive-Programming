'''
https://leetcode.com/problems/vowels-of-all-substrings/
'''

class Solution:
    def countVowels(self, word: str):
        n = len(word)
        ans = 0
        vowelSet = {'a', 'e', 'i', 'o', 'u'}

        for i in range(n):
            ch = word[i]
            if ch in vowelSet:
                right_char_no = n - i
                ans +=(i * right_char_no) + right_char_no

        return ans
