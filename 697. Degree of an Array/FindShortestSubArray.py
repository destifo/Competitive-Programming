from typing import Counter, List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: hashtable, 
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_freq = max(count.values())
        max_freq_nums = set()
        
        for num, cnt in count.items():
            if cnt == max_freq:
                max_freq_nums.add(num)
                
        first_occurence = {}
        last_occurence = {}
        
        for i, num in enumerate(nums):
            if num in max_freq_nums and num not in first_occurence:
                first_occurence[num] = i
                
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            
            if num in max_freq_nums and num not in last_occurence:
                last_occurence[num] = i
                
        shortest = len(nums)
        
        for num in max_freq_nums:
            shortest = min(shortest, last_occurence[num]-first_occurence[num]+1)
            
        return shortest