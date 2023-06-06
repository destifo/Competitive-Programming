from typing import List


class Solution:
    # O(nums1.length + nums2.length) time,
    # O(nums2.length) space,
    # Approach: monotonic stack, hashmap
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        for index, num in enumerate(nums2):
            
            while stack and num > nums2[stack[-1]]:
                popped_index = stack.pop()
                next_greater[nums2[popped_index]] = num
            stack.append(index)
        
        
        ans = []
        for num in nums1:
            if num in next_greater:
                ans.append(next_greater[num])
            else:
                ans.append(-1)
                
        return ans