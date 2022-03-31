class Solution:
    def fib(self, n: int):
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    def fib2(self, n: int):
        if n < 2:
            return n
        a_0 = 0
        a_1 = 1
        curr = 0
        for i in range(n - 1):
            curr = a_0 + a_1
            a_0 = a_1
            a_1 = curr
        
        return curr


sol = Solution()
print(sol.fib2(4))