class Solution:
    def uniquePaths(self, m: int, n: int):
        memo = {}
        def calcUnique(a,b):
            if a == m - 1 and b == n - 1:
                return 1
            
            if a >= m or b >= n:
                return 0
            
            if not memo.get((a + 1, b), None):
                memo[(a + 1, b)] = calcUnique(a + 1, b)
            if not memo.get((a, b + 1), None):
                memo[(a, b + 1)] = calcUnique(a, b + 1)
            return memo[(a + 1, b)] + memo[(a, b + 1)]
        
        return calcUnique(0, 0)
