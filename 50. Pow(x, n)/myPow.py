'''
https://leetcode.com/problems/powx-n/submissions/https://leetcode.com/problems/powx-n/submissions/
'''

class Solution:
    # solved this one on my own, no help at all...
    def myPow(self, x: float, n: int):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        
        if n > 1:
            if n % 2 == 0:
                return self.myPow(x, n//2) ** 2
            else:
                return x * (self.myPow(x, n//2) ** 2)
        if n < -1:
            n *= -1
            if n % 2 ==0:
                return self.myPow(x, (n//2) * -1) ** 2
            else:
                return 1/x * (self.myPow(x, (n//2) * -1) ** 2)

    # modified the upper one and leetcode says it's faster
    def myPow2(self, x: float, n: int):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        
        if n > 1:
            return (self.myPow(x, n//2) ** 2) if (n % 2 == 0) else x * self.myPow(x, n//2) ** 2
        if n < -1:
            n *= -1
            return (1/x * self.myPow(x, -1 * (n//2)) **2) if (n % 2 != 0) else (self.myPow(x, -1*(n//2))**2 )


sol = Solution()
print(sol.myPow(2,-2))