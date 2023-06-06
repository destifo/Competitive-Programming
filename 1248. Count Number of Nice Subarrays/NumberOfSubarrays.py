'''
https://leetcode.com/problems/count-number-of-nice-subarrays/submissions/
'''

class Solution:
    # an O(n) solution, the same as the question SubarraySum, did it fast, feeling good.
    def numberOfSubarrays(self, nums, k: int):
        n = len(nums)
        prefixSumCount = dict()
        prefixSumCount[0] = 1
        currSum = 0
        result = 0
        for num in nums:
            currVal = self.assignParity(num)
            currSum += currVal
            diff = currSum - k
            if diff in prefixSumCount.keys():
                result += prefixSumCount[diff]
            prefixSumCount[currSum] = prefixSumCount.get(currSum, 0) + 1

        return result

            

    def assignParity(self, num):
        if num % 2 == 0:
            return 0
        return 1