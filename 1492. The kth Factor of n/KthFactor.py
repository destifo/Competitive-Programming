import math


class Solution:
    # O(sqrt(n)) time,
    # O(sqrt(n)) space,
    # Approach: math, array
    def kthFactor(self, n: int, k: int) -> int:
        second_half = []
        num_sqrt = math.ceil(math.sqrt(n))
        
        for f in range(1, num_sqrt+1):
            if n % f != 0:  continue
            k -=1
            if k == 0:  return f
            d = n//f
            if d > f:
                second_half.append(d)
            
        if f == second_half[-1]:
            second_half.pop()
            
        return second_half[-k] if k <= len(second_half) else -1