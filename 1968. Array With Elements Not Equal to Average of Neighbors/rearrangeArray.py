'''
https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/submissions/
'''

class Solution:
    def rearrangeArray(self, nums):
        nums.sort()
        nums_length = len(nums)
        result = [0]*nums_length
        if nums_length % 2 != 0:
            for i in range((nums_length//2) + 1):
                result[i*2] = nums[i]
            j = 1
            for i in range(nums_length//2 + 1, nums_length):
                result[j] = nums[i]
                j +=2
        else:
            for i in range((nums_length//2)):
                result[i*2] = nums[i]
            j = 1
            for i in range(nums_length//2, nums_length):
                result[j] = nums[i]
                j +=2
        return result


sol = Solution()
print(sol.rearrangeArray([1,2,3,4,5]))