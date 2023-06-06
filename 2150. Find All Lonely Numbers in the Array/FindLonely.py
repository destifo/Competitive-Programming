from typing import List


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: hashtable, 
    def findLonely(self, nums: List[int]) -> List[int]:
        nums_count = {}
        ans = []
        
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
            
        for num, count in nums_count.items():
            if count > 1:   continue
            if (num-1) in nums_count or (num+1) in nums_count:
                continue
            
            ans.append(num)
            
        return ans

    
    # O(n) time,
    # O(1) space,
    # Approach: hashtable, 
    def findLonely(self, nums: List[int]) -> List[int]:
        ans = []
        
        nums.sort()
        
        for index, num in enumerate(nums):
            if index == 0:
                if len(nums) < 2 or nums[index+1]-num > 1:
                    ans.append(num)
            elif index == len(nums)-1:
                if num-nums[index-1] > 1:
                    ans.append(num)
            else:
                if num-nums[index-1] > 1 and nums[index+1]-num > 1:
                    ans.append(num)
                    
        return ans