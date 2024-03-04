'''
https://leetcode.com/problems/bag-of-tokens/
'''


from typing import List


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: two pointers, greedy, sorting
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        tokens.sort()
        
        l, r = 0, n
        curr_score = 0
        max_score = curr_score
        
        while l < r:
            if power >= tokens[l]:
                curr_score +=1
                power -= tokens[l]
                l +=1
            else:
                r -=1
                if curr_score <= 0:   break
                curr_score -=1
                power += tokens[r]
                
            max_score = max(max_score, curr_score)
            
        return max_score
    
    
    # O(nlogn) time,
    # O(1) space,
    # Approach: greedy, sorting, two pointers
    def bagOfTokensScore2(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        left, right = 0, len(tokens)-1
        max_score = 0
        score = 0
        
        
        while left <= right:
            if score > 0 and power < tokens[left]:
                power += tokens[right]
                right -= 1
                score -= 1
            
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1
            else:
                break
                
            max_score = max(max_score, score)
        
        return max_score


sol = Solution()
print(sol.bagOfTokensScore([100,200,300,400]
,200))