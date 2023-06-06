from typing import List


class Solution:
    # O(nlogn) time,
    # O(1) space,
    # Approach: sorting, 
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        limit = nums[0] + k
        subseqs = 1
        
        for num in nums:
            if num > limit:
                limit = num + k
                subseqs +=1
                
        return subseqs