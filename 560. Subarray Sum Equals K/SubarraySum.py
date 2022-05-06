'''
https://leetcode.com/problems/subarray-sum-equals-k/
'''

class Solution:
    def subarraySum(self, nums, k: int):
        n = len(nums)
        pfSumMap = dict()
        pfSumMap[0] = 1

        result = 0
        currSum = 0
        for num in nums:
            currSum += (num - k)
            if currSum in pfSumMap.keys():
                result += pfSumMap[currSum]
            pfSumMap[currSum] = pfSumMap.get(currSum, 0) + 1

        return result
        