'''
https://leetcode.com/problems/delete-and-earn/
'''


from collections import Counter


class Solution:
    # less optmial solution, but still passes on submission, almost converted in to the house robber problem
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

    
    # optimal solution 
    # O(logn + m) time complexity, cause we are sorting the keys(distinct nums), m(original nums array length) for building the dictionary
    # O(m + n) for the map and the dp array
    def deleteAndEarn2(self, nums: list[int]) -> int:
        nums_count = Counter(nums)
        nums = sorted(nums_count.keys())
        n = len(nums)
        dp = [0] * n
        
        for i in range(n):
            num = nums[i]
            tot = nums_count[num] * num
            if i == 0:
                dp[i] = tot
            elif i == 1:
                dp[i] = max(tot, dp[i-1]) if nums[i-1] == num-1 else tot + dp[i-1]
            else:
                dp[i] = max(tot + dp[i-2], dp[i-1]) if nums[i-1] == num-1 else tot + dp[i-1]
                
        
        return dp[n-1]