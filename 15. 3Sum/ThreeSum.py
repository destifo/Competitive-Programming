'''
https://leetcode.com/problems/3sum/
'''


class Solution:
    # O(n^2) time,
    # O(len(ans)) space,
    # Approach: Two pointers
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        
        nums.sort()
        
        for i in range(n-2):
            fixed = nums[i]
            if i > 0 and fixed == nums[i-1]:
                continue
            l, r = i + 1, n-1
            tot = fixed + nums[l] + nums[r]
            while l < r:
                if tot == 0:
                    ans.append([fixed, nums[l], nums[r]])
                    tot -= nums[r]
                    r -=1
                    tot += nums[r]
                    while r > l and nums[r] == nums[r+1]:
                        tot -= nums[r]
                        r -=1
                        tot += nums[r]
                elif tot > 0:
                    tot -= nums[r]
                    r -=1
                    tot += nums[r]
                else:
                    tot -=nums[l]
                    l +=1
                    tot +=nums[l]
                    
        return ans