class Solution:
    
    # O(sqrt(n)*logn) time,
    # O(1) space,
    # Approach: math, 
    def consecutiveNumbersSum(self, n: int) -> int:
        while n % 2 == 0:
            n //=2
            
        ans = 1
        curr = 3    # current odd
        while (curr**2) <= n:
            count = 1   # start with that additional one
            while n % curr == 0:
                count += 1
                n //=curr
                
            ans *= count
            curr += 2
        
        # n is divisible by the last curr odd, but wasn't not computed in to ans, we compute here
        if n != 1:
            ans *= 2
            
        return ans