'''
https://leetcode.com/problems/count-sorted-vowel-strings/
'''

class Solution:
    # naive solution but passed the test
    def countVowelStrings(self, n: int):

        def dfs(i, leng):
            if i == 5:
                return 0

            if leng == n:
                return 1

            return dfs(i, leng + 1) + dfs(i + 1, leng)
        
        return dfs(0, 0)

    
    def countVowelStrings2(self, n: int):
        def dfs(i, leng):
            if i == 5:
                return 0

            if leng == n:
                return 1

            return dfs(i, leng + 1) + dfs(i + 1, leng)
        
        return dfs(0, 0)
