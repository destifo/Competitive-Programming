'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

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


sol = Solution()
print(sol.letterCombinations2('235'))