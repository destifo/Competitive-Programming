'''
https://leetcode.com/problems/find-the-middle-index-in-array/
'''


class Solution:
    def findMiddleIndex(self, nums: list[int]):
        n = len(nums)
        left_prefix = [0] * (n + 1)
        right_prefix = [0] * (n + 1)

        tot = 0
        for i in range(n):
            tot += nums[i]
            left_prefix[i + 1] = tot
        
        tot = 0
        for i in range(n-1, -1, -1):
            tot +=nums[i]
            right_prefix[i - 1] = tot

        for i in range(n):
            if right_prefix[i] == left_prefix[i]:
                return i

        return -1


sol = Solution()
print(sol.findMiddleIndex([2,3,-1,8,4]))