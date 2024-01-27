class Solution:
     
    # O(n*k) time,
    # O(n*k) space,
    # Approach: dp, sliding window
    def kInversePairs(self, n: int, k: int) -> int:
        prev = [0 for _ in range(k+1)]
        prev[0] = 1
        MOD = 10**9 + 7
        
        for i in range(n):
            curr = [0 for _ in range(k+1)]
            tot = 0
            for right in range(0, k+1):
                left = right-i-1
                if left >= 0:
                    tot -= prev[left]
                tot += prev[right]
                curr[right] = tot
            prev = curr
            
        return curr[k] % MOD