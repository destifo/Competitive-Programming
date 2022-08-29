'''
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
'''


from collections import Counter


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: monotonic stack, greedy, hashtable
    def smallestSubsequence(self, s: str) -> str:
        count = Counter(s)
        vstd = set()
        
        stack = []
        for ch in s:
            if ch in vstd:
                count[ch] -=1
                continue
            while stack and stack[-1] > ch and count[stack[-1]] > 0:
                vstd.remove(stack.pop())
            
            stack.append(ch)
            vstd.add(ch)
            count[ch] -=1
            
        return "".join(stack)