class Solution:
    def isPowerOfThree(self, n: int):
        if n == 3 or n == 1:
            return True
        if n < 3 or (n % 3) != 0:
            return False
        return self.isPowerOfThree(n/3)

sol = Solution()
print(sol.isPowerOfThree(27))