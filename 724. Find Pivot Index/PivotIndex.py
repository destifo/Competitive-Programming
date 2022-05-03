'''
https://leetcode.com/problems/find-pivot-index/submissions/
'''

class Solution:
    def pivotIndex(self, nums):
        n = len(nums)
        prefixSum = [0] * (n+1)

        currSum = 0
        for index,num in enumerate(nums):
            currSum +=num
            prefixSum[index + 1] = currSum

        for i in range(1, n + 1):
            leftSum = prefixSum[i - 1]
            rightSum = prefixSum[n] - prefixSum[i]
            if leftSum == rightSum:
                return i - 1

        return -1