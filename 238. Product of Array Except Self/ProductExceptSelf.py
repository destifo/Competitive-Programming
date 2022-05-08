'''
https://leetcode.com/problems/product-of-array-except-self/
'''

class Solution:
    # prefix is ezy to grasp..., catching upto these questions with little time and less errors now
    def productExceptSelf(self, nums):
        n = len(nums)
        prefixProd = [1] * (n + 1)
        postfixProd = [1] * (n + 1)
        currProd = 1
        for i in range(n):
            currProd *= nums[i]
            prefixProd[i + 1] = currProd

        currProd = 1
        for i in range(n - 1, -1, -1):
            currProd *= nums[i]
            postfixProd[i] = currProd

        result = [1] * n
        for i in range(1, n + 1):
            preProd = prefixProd[i - 1]
            postProd = postfixProd[i]
            prod = preProd * postProd
            result[i - 1] = prod

        return result

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))