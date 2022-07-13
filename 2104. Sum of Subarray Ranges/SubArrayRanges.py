'''
https://leetcode.com/problems/sum-of-subarray-ranges/
'''


class Solution:
    # O(n^2) time,
    # O(1) space
    def subArrayRanges(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        
        for i in range(n):
            minm = nums[i]
            maxm = nums[i]
            for j in range(i, n):
                minm = min(minm, nums[j])
                maxm = max(maxm, nums[j])
                ans +=(maxm-minm)
                
        return ans


    # The intution behind this solution is genius
    # O(n) time
    # O(n) space
    def subArrayRanges2(self, nums: list[int]) -> int:
        n = len(nums)
        tot = 0

        inc_stack = []
        dec_stack = []

        def pushToIncStack(index:int, stack:list) -> int:
            tot = 0
            num = nums[index]
            while stack and nums[stack[-1]] > num:
                curr_i = stack.pop()
                prev_i = stack[-1] if stack else -1
                tot += (curr_i - prev_i) * (index - curr_i) * nums[curr_i]

            stack.append(i)

            return tot

        def pushToDecStack(index:int, stack:list) -> int:
            tot = 0
            num = nums[index]
            while stack and nums[stack[-1]] < num:
                curr_i = stack.pop()
                prev_i = stack[-1] if stack else -1
                tot += (curr_i - prev_i) * (index - curr_i) * nums[curr_i]

            stack.append(i)

            return tot

        def popAll(index:int) -> int:
            min_sum = 0
            max_sum = 0

            stack = dec_stack
            while stack:
                curr_i = stack.pop()
                prev_i = stack[-1] if stack else -1
                max_sum += (curr_i - prev_i) * (index - curr_i) * nums[curr_i]

            stack = inc_stack
            while stack:
                curr_i = stack.pop()
                prev_i = stack[-1] if stack else -1
                min_sum += (curr_i - prev_i) * (index - curr_i) * nums[curr_i]

            return max_sum - min_sum

        for i in range(n):
            sub_min_sum = pushToIncStack(i, inc_stack)
            sub_max_sum = pushToDecStack(i, dec_stack)
            tot +=(sub_max_sum - sub_min_sum)

        tot +=popAll(n)

        return tot


sol = Solution()
print(sol.subArrayRanges2([4,-2,-3,4,1]))