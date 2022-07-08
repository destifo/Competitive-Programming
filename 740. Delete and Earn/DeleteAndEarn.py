'''
https://leetcode.com/problems/delete-and-earn/
'''


class Solution:
    # less optmial solution
    def deleteAndEarn(self, nums: list[int]) -> int:
        n = 10001
        nums_count = [0] * n
        
        for num in nums:
            # if nums_count[num] == 0:
            #     n +=1
            nums_count[num] +=1
            
        dp = [0] * n
        for i in range(n-1, -1, -1):
            if i > n-3:
                dp[i] = nums_count[i] * i
            elif i == n-3:
                dp[i] = dp[i+2] + nums_count[i] * i
            else:
                dp[i] = max(dp[i+2], dp[i+3]) + nums_count[i] * i
        
        return max(dp[0], dp[1])