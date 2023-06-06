'''
https://leetcode.com/problems/numbers-with-same-consecutive-differences/
'''


from typing import List


class Solution:
    # O(10^n) time,
    # O(n*10^n) space,
    # Approach: backtracking, dfs
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        
        def dfs(lst, leng):
            if leng == n:
                ans.append(int(''.join(list(map(str, lst)))))
                return
                
            for i in range(0, 10):
                if abs(lst[-1] - i) == k:
                    lst.append(i)
                    dfs(lst, leng+1)
                    lst.pop()
            
        for i in range(1, 10):
            dfs([i], 1)
            
        return ans