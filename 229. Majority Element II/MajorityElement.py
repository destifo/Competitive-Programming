'''
https://leetcode.com/problems/majority-element-ii/
'''


class Solution:
    # O(n) time
    # O(n) space
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = []
        nums_count = dict()
        
        for num in nums:
            count = nums_count.get(num, 0)
            if count == 'added':
                continue
            nums_count[num] = count + 1
            if nums_count[num] > n // 3:
                result.append(num)
                nums_count[num] = 'added'
                
        return result


    # O(nlogn) time
    # O(1) space, as per the leetcode follow up
    def majorityElement2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = []
        least_len = (n // 3) + 1
        l, r = 0, least_len-1
        
        nums.sort()
        
        while r < n:
            if nums[l] == nums[r]:
                if not result or result[-1] != nums[l]:
                    result.append(nums[l])
                if len(result) > 2:
                    return result
            l +=1
            r +=1
            
        return result