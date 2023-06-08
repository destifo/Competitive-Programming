from typing import List


class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: brain-teaser, array
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
        answer = 0
        right_most_flipped = -1
        for i, bit_pos in enumerate(flips):
            right_most_flipped = max(right_most_flipped, bit_pos)
            if i+1 == right_most_flipped:
                answer += 1
                
        return answer