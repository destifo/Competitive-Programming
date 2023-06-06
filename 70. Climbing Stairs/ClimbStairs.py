'''
https://leetcode.com/problems/climbing-stairs/
'''

class Solution:
    def climbStairs(self, n: int):
        # naive solution+
        def findNumOfStrairs(rem, tot):
            if tot == n:
                return 1
            
            if tot > n:
                return 0

            return findNumOfStrairs(rem - 1, tot + 1) + findNumOfStrairs(rem - 2, tot + 2)

        return findNumOfStrairs(n, 0)

    
    def climbStairs2(self, n: int):
        # efficent algorithm using memoization
        memo = dict()
        def findNumOfStairs(rem, tot):
            if tot == n:
                return 1

            if tot > n:
                return 0

            if not memo[rem - 1]:
                memo[rem - 1] = findNumOfStairs(rem - 1, tot - 1)

            if not memo[rem - 2]:
                memo[rem - 2] = findNumOfStairs(rem - 2, tot - 2)

            return memo[rem - 1] + memo[rem - 2]

        return findNumOfStairs(n, 0)

    
    # iterative approach, the sequence is the same as the fibonacci numbers from my observation
    def climbStairs3(self, n: int):
        if n < 3:
            return n
        
        a_1 = 1
        a_2 = 2
        curr = a_1 + a_2
        for i in range(3, n+1):
            curr = a_1 + a_2
            a_1 = a_2
            a_2 = curr
            
        return curr