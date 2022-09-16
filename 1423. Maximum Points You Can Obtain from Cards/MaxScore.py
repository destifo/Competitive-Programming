'''
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
'''


from typing import List


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: sliding window, two pointers, 
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        tot_sum = sum(cardPoints)
        if k == n:
            return tot_sum
        
        l, r = 0, n-k
        curr_score = tot_sum - sum(cardPoints[l:r])
        max_score = curr_score
        
        while r < n:
            curr_score += cardPoints[l]
            curr_score -= cardPoints[r]
            
            l +=1
            r +=1
            max_score = max(max_score, curr_score)
            
        return max_score