class Solution:
    # O(4^n) time, because our depth can go 2*n
    # have
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        
        def backtrack(open, closed, arr):
            if open == closed and open == n:
                ans = "".join(arr)
                result.append(ans)
                return
            
            if open < n:
                arr.append('(')
                backtrack(open+1, closed, arr.copy())
                arr.pop()
            if closed < open:
                arr.append(')')
                backtrack(open, closed+1, arr.copy())
            return
                
        backtrack(0, 0, [])
        
        return result


sol = Solution()
print(sol.generateParenthesis(6))