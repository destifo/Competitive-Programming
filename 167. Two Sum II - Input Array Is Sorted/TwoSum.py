'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''

class Solution:
    def twoSum(self, numbers, target: int):
        # brute force
        n = len(numbers)
        l, r = 0, n - 1
        while r > 0:
            while numbers[l] + numbers[r] > target:
                r -=1

            currL = l
            while currL < r:
                if numbers[l] + numbers[r] == target:
                    return [l + 1, r + 1]
                
                currL +=1

            l +=1

    def twoSum2(self, nums, target: int):
        # optimal soultion
        n = len(nums)
        l, r = 0, n - 1
        tot = nums[l] + nums[r]
        while tot != target:
            if tot < target:
                tot -=nums[l]
                l +=1
                tot += nums[l]
            else:
                tot -=nums[r]
                r -=1
                tot +=nums[r]

        return [l + 1, r + 1]

    
    # just different code when I did it on another day
    def twoSum3(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        l, r = 0, n-1
        
        val = nums[l] + nums[r]
        while l < r:
            if val == target:
                return [l+1, r+1] # 1 indexed answer
            elif val > target:
                val -=nums[r]
                r -=1
                val +=nums[r]
            else:
                val -=nums[l]
                l +=1
                val +=nums[l]
                
        return [-1, -1]


sol = Solution()
print(sol.twoSum2([2,7,11,15],9))