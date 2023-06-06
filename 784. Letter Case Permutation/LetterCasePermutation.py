'''
https://leetcode.com/problems/letter-case-permutation/
'''


from typing import List


class Solution:
    # honestly, this backtracking question is where I unnderstood backtracking, hopefully
    def letterCasePermutation(self, s: str) -> list[str]:
        result = []
        result.append(s)
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


    def findLetterPermutations(self, index: int, word: str, curr_list: List[str], answer: List[str]) -> None:
        
        if index == len(word):
            permutation = ''.join(curr_list)
            answer.append(permutation)
            return
        
        ch = word[index]
        if ch.isdigit():
            curr_list.append(ch)
            self.findLetterPermutations(index+1, word, curr_list, answer)
            curr_list.pop()
        else:
            # upper case
            curr_list.append(ch.upper())
            self.findLetterPermutations(index+1, word, curr_list, answer)
            curr_list.pop()
            
            # lower case
            curr_list.append(ch.lower())
            self.findLetterPermutations(index+1, word, curr_list, answer)
            curr_list.pop()
    
    
    # O(2^n) time,
    # O(2^n) space,
    # Approach: backtracking, recursion
    def letterCasePermutation2(self, s: str) -> List[str]:
        
        answer = []
        
        self.findLetterPermutations(0, s, [], answer)
        
        return answer