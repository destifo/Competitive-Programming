class Solution:
    def maxProduct(self, nums):
        currmax, currmin = 1, 1

        for num in nums:
            if num == 0:
                currmax, currmin = 1, 1

            oldmax = currmax
            currmax = max(oldmax * num, currmin * num, num)
            currmin = min(oldmax * num, currmin * num, num)

        return currmax

    
sol = Solution()
print(sol.maxProduct([-2, -1, -3]))