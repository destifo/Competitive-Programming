'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

from typing import Dict, List


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        n = len(digits)
        numToDigits = [0] * 10
        numToDigits[2] = "abc"
        numToDigits[3] = "def"
        numToDigits[4] = "ghi"
        numToDigits[5] = "jkl"
        numToDigits[6] = "mno"
        numToDigits[7] = "pqrs"
        numToDigits[8] = "tuv"
        numToDigits[9] = "wxyz"

        ans = []
        for digit in digits:
            curr = []
            for ch in numToDigits[int(digit)]:
                curr.append(ch)
            ans.append(curr)

        l = 0
        while l < (n - 1):
            ans[l + 1] = self.combine(ans, l, l + 1)
            l +=1

        return ans[l]
    
    def combine(self, lst, index1, index2):
        result = []
        for elt1 in lst[index1]:
            for elt2 in lst[index2]:
                wrd = ""
                wrd += elt1
                wrd += elt2
                result.append(wrd)

        return result


    def letterCombinations2(self, digits):
        if not digits:
            return []

        n = len(digits)
        numToDigits = [0] * 10
        numToDigits[2] = "abc"
        numToDigits[3] = "def"
        numToDigits[4] = "ghi"
        numToDigits[5] = "jkl"
        numToDigits[6] = "mno"
        numToDigits[7] = "pqrs"
        numToDigits[8] = "tuv"
        numToDigits[9] = "wxyz"

        ans = []
        for digit in digits:
            curr = []
            for ch in numToDigits[int(digit)]:
                curr.append(ch)
            ans.append(curr)

        l = n - 2
        while l > -1:
            ans[l] = self.combine(ans, l, l + 1)
            if len(ans) > 1:
                ans.pop()
            l -=1

        return ans[0]

    
    def findCombinations(self, index: int, digits: str, keys: Dict[str, str], curr: List[str], ans: List[str]) -> None:
        
        if index == len(digits):
            ans.append("".join(curr))
            return
        
        digit = digits[index]
        for ch in keys[digit]:
            curr.append(ch)
            self.findCombinations(index+1, digits, keys, curr, ans)
            curr.pop()
    
    # O(4^n) time, n --> len(digits)
    # O(4^n) space,
    # Approach: backtracking, recursion
    def letterCombinations2(self, digits: str) -> List[str]:
        keys = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        ans = []
        if digits:  self.findCombinations(0, digits, keys, [], ans)
        return ans