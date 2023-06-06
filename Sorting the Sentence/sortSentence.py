"""
https://leetcode.com/problems/sorting-the-sentence/submissions/
"""

class Solution:
    def sortSentence(self, s: str) -> str:
        str = s.split()
        str_lst = [0] * 10
        for word in str:
            str_lst[int(word[-1])] = word[:-1] + " "
        final_str = ""
        for word in str_lst:
            if (word != 0):
                final_str += word
        return final_str.rstrip()

sol = Solution()
sol.sortSentence("is2 sentence4 This1 a3")