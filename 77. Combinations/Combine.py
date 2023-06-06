class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        combinations = []
        
        def dfs(num, arr):
            # if num == n:
            #     return
            if len(arr) == k:
                combinations.append(arr.copy())
                return
            
            for i in range(num, n+1):
                arr.append(i)
                dfs(i+1, arr)
                arr.pop()
            
        dfs(1, [])
        
        return combinations


sol = Solution()
print(sol.combine(4, 2))