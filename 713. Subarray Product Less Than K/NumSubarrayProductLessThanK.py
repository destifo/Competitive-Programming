class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int):
        n = len(nums)
        ans = 0
        
        l, r = 0, 0
        currProd = nums[0]
        while r < n:
            while currProd >= k:
                currProd /= nums[l]
                l +=1
            
            ans += r - l + 1
            r +=1
            if r < n:   currProd *= nums[r]

            
        return ans


sol = Solution()
print(sol.numSubarrayProductLessThanK([10,5,2,6], k = 100))