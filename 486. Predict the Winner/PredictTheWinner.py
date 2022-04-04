'''
https://leetcode.com/problems/predict-the-winner/submissions/
'''

# interesting puzzle with an intersting solution
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


sol = Solution()
print(sol.PredictTheWinner([1,5,2,4,6]))