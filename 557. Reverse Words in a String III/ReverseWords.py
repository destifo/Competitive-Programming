'''
https://leetcode.com/problems/reverse-words-in-a-string-iii/
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        def reverseString(st: list[str]) -> None:
            n = len(st)
            l, r = 0, n-1

            while l < r:
                if st[l] != st[r]:
                    temp = st[l]
                    st[l] = st[r]
                    st[r] = temp
                l +=1
                r -=1
            
            return st
        
        for word in s.split():
            rev_word = "".join(reverseString(list(word)))
            result +=rev_word
            result +=" "
        
        return result.strip()