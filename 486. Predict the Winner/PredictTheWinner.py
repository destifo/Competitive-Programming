'''
https://leetcode.com/problems/predict-the-winner/submissions/
'''

# interesting puzzle with an intersting solution
from typing import Dict, List, Tuple


class Solution:
    def PredictTheWinner(self, nums):
        n = len(nums)
        maxval = self.findWinner(nums, 0, n - 1, True, 0)
        if maxval >= 0:
            return True
        return False

        
    def findWinner(self, nums, start, end, turn, score):
        if start == end:
            if turn:
                score += nums[start]
            else:
                score -= nums[start]
            return score
            
        
        if turn:
            return max(self.findWinner(nums, start + 1, end, False, score + nums[start]), self.findWinner(nums, start, end - 1, False, score + nums[end]))
        else:
            return min(self.findWinner(nums, start + 1, end, True, score - nums[start]), self.findWinner(nums, start, end - 1, True, score - nums[end]))
        
    
    def predict(self, start: int, end: int, nums: List[int], first: bool, memo: Dict[Tuple[int], int]) -> Tuple[int]:
        
        if start > end:
            return (0, 0)
        
        state = (start, end, first)
        if state in memo:
            return memo[state]
        
        
        if first:
            take_first = tuple(map(lambda i, j: i + j, (nums[start], 0), self.predict(start+1, end, nums, not first, memo)))
            take_last = tuple(map(lambda i, j: i + j, (nums[end], 0), self.predict(start, end-1, nums, not first, memo)))
            memo[state] = take_first if take_first[0] > take_last[0] else take_last
        else:
            take_first = tuple(map(lambda i, j: i + j, (0, nums[start]), self.predict(start+1, end, nums, not first, memo)))
            take_last = tuple(map(lambda i, j: i + j, (0, nums[end]), self.predict(start, end-1, nums, not first, memo)))
            
            memo[state] = take_first if take_first[1] > take_last[1] else take_last
            
        return memo[state]
    
    
    
    # O(n^2) time,
    # O(n) space,
    # Approach: min-max algo, top down dp, 
    def PredictTheWinner(self, nums: List[int]) -> bool:
        first, second = self.predict(0, len(nums)-1, nums, True, {})
        # print(first, second)
        return first >= second


sol = Solution()
print(sol.PredictTheWinner([1,5,2,4,6]))