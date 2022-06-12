'''
https://leetcode.com/problems/sort-characters-by-frequency/
'''


from collections import Counter


class Solution:
    def frequencySort(self, s: str):
        char_count = Counter(s)
        char_count = sorted(char_count.items(), key=lambda x:x[1], reverse=True)
        
        ans = ''
        for char, freq in char_count:
            for i in range(freq):
                ans +=char
                
        return ans