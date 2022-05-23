from collections import Counter

class Solution:
    def findMaxForm(self, strs, m: int, n: int):
        memo = {}
        nums_count = []
        for s in strs:
            nums_count.append(Counter(s))

        for index,s in enumerate(strs):
            for i in range(m, nums_count[index].get('0', 0) - 1, -1):
                for j in range(n, nums_count[index].get('1', 0) - 1, -1):
                    memo[(i, j)] = max(memo.get((i - nums_count[index].get('0', 0), j - nums_count[index].get('1', 0)), 0) + 1, memo.get((i, j), 0))

        return memo.get((m, n), 0)

sol = Solution()
print(sol.findMaxForm(["001", "110","0000","0000"],9,2))