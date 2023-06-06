'''
https://leetcode.com/problems/top-k-frequent-words/
'''


from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int):
        n = len(words)
        freq = [set() for i in range(n)]
        nums_count = Counter(words)
        
        for key, value in nums_count.items():
            freq[value].add(key)
            
        result = []
        for i in range(n-1, -1, -1):
            if len(freq[i]) > 0 and k > 0:
                freq[i] = sorted(freq[i])
                for word in freq[i]:
                    if k < 1:   return  result
                    result.append(word)
                    k -=1
        
        return result
        