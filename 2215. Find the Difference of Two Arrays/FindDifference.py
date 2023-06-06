from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: hash table, 
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]
        
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        
        for num in nums1:
            if num not in nums2_set:
                answer[0].append(num)
                nums2_set.add(num)
                
        for num in nums2:
            if num not in nums1_set:
                answer[1].append(num)
                nums1_set.add(num)
                
        return answer