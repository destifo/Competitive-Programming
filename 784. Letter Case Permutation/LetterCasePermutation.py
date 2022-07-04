'''
https://leetcode.com/problems/letter-case-permutation/
'''


class Solution:
    # honestly, this backtracking question is where I unnderstood backtracking, hopefully
    def letterCasePermutation(self, s: str) -> list[str]:
        result = []
        alpha_indices = []
        for index,ch in enumerate(s):
            if ch.isalpha():
                alpha_indices.append(index)
        
        def backtrack(index:int, st:str):
            if index >= len(alpha_indices):
                return
            
            i = alpha_indices[index]
            mod_letter = st[i].upper() if st[i].islower() else st[i].lower()
            new_str = st[:i] + mod_letter + st[i+1:]
            result.append(new_str)
            backtrack(index+1, new_str)
            backtrack(index+1, st)

        backtrack(0, s)

        return result