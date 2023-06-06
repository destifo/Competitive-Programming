from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: prefix sum, math
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        '''
        intution: the trick here is that noticing that you can 
        if you substract two numbers, say a and b, both having the
        same mod by k, their difference will be divisible by k
        
        for eg take, 13 and 7, mod 6 are both 1, if u find the abolute value of these two, it will be 13-7=6. 
        
        so what we can do here is to find prefix sum at each index and group
        sums with the same mod(sum till an index % k), and find the number of pairs
        '''
        
        # store previous (tot%k) values and
        group = [0 for _ in range(k)]
        group[0] = 1
        tot = 0
        answer = 0
        for num in nums:
            tot += num
            # if we find any sums before this index, with the same value when moded by k, 
            # we pair this one to the previous sums
            answer += group[tot%k]
            group[tot%k] += 1
            
        # return answer
        return answer