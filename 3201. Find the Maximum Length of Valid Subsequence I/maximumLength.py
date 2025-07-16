from typing import List


class Solution:

    # O(n) time,
    # O(n) space, since I'm using that list for the sum
    # Approach: counting, math
    def maximumLength(self, nums: List[int]) -> int:
        
        """
        parity: we can use 0 or 1, 

        choice 1: take current num (if its the first num and second num we take
            or if it satisfies the parity check) or else skip
        
        choice 2: skip the number

            OR

        case 1: odd + odd = even (odd + odd + odd) counting odds
        case 2: even + even = even (even + even + even) counting evens
        case 3: odd + even = odd (odd + even + odd) or (even + odd + even)
        
        """
        
        case1 = sum(1 for num in nums if num % 2 == 1)
        case2 = sum(1 for num in nums if num % 2 == 0)
        
        case3 = 0
        curr_parity = 0
        curr = 0
        for num in nums:
            if num % 2 == curr_parity:
                curr += 1
                curr_parity += 1
                curr_parity %= 2
        
        case3 = max(case3, curr)
        curr = 0
        curr_parity = 1
        for num in nums:
            if num % 2 == curr_parity:
                curr += 1
                curr_parity += 1
                curr_parity %= 2
        case3 = max(case3, curr)

        return max(case1, case2, case3)
        


