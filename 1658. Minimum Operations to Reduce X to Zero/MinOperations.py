'''
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
'''


from typing import List


class Solution:

    # an O(2^n) recursive solution 
    def minOperations(self, nums: list[int], x: int):
        def dfs(rem, curr_len, l, r):
            if rem == 0:
                return curr_len
            
            if rem < 0:
                return float('inf')
            
            chose_left = dfs(rem - nums[l], curr_len + 1, l + 1, r)
            chose_right = dfs(rem-nums[r], curr_len + 1, l, r - 1)
            return min(chose_left, chose_right)
        
        ans = dfs(x, 0, 0, len(nums) - 1)
        return -1 if ans == float('inf') else ans
                
    
    # using a memoization, slightly better but still gives TLE
    def minOperations2(self, nums: list[int], x: int):
        memo = {}
        def dfs(rem, curr_len, l, r):
            if rem == 0:
                return curr_len
            
            if rem < 0:
                return float('inf')
            
            key = str(l) + '#' + str(r) + '#' + str(curr_len)
            if key in memo.keys():
                return memo[key]

            chose_left = dfs(rem - nums[l], curr_len + 1, l + 1, r)
            chose_right = dfs(rem-nums[r], curr_len + 1, l, r - 1)
            memo[key] = min(chose_left, chose_right)
            return memo[key]
        
        ans = dfs(x, 0, 0, len(nums) - 1)
        return -1 if ans == float('inf') else ans


    # an O(n) solution using two pointer, it really made me sweat to implement,
    # with the edge cases and stuff..., and the reverse thinking to find the 
    # the longest subarray with the sum(nums) - x, which helps u to find the min subarray with the sum x in reverse...crazy stuff :-}
    def minOperations3(self, nums: list[int], x: int):
        n = len(nums)
        if n == 1:
            return 1 if nums[0] == x else -1

        prefix_sum = [0] * (n+1)

        tot = 0
        for i in range(n):
            tot +=nums[i]
            prefix_sum[i + 1] = tot

        nums_sum = prefix_sum[n] - x
        if nums_sum < 0:    return -1
        if nums_sum == 0:   return n
        tot = nums[0]
        max_len = 0
        l, r = 0, 1 
        while r < n:
            if tot == nums_sum:
                max_len = max(max_len, r - l)
            if tot >= nums_sum:
                tot -=nums[l]
                l +=1
                continue
            
            num = nums[r]
            tot +=num
            while tot > nums_sum:
                tot -=nums[l]
                l +=1 
            r +=1
        if tot == nums_sum:
            max_len = max(max_len, r - l)

        return n - max_len if max_len else -1
    
    
    # O(n) time,
    # O(n) space,
    # Approach: two sum hash map, 
    def minOperations4(self, nums: List[int], x: int) -> int:
        n = len(nums)
        cache = {0: 0}
        
        tot = 0
        for i in range(n-1, -1, -1): 
            tot += nums[i]
            if tot > x:
                break
            cache[tot] = n-i
            
        ans = cache[x] if x in cache else float('inf')
        tot = 0
        for i, num in enumerate(nums):
            tot += num
            if tot > x:
                break
            if x-tot in cache and n-cache[x-tot] > i:
                length = i + cache[x-tot] + 1
                ans = min(ans, length)
                
        return ans if ans != float('inf') else -1
            

sol = Solution()
print(sol.minOperations3([5,1,4,2,3], 6))