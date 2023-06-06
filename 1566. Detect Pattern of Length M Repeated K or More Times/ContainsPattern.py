from typing import List


class Solution:
    
    def serializePattern(self, nums) -> str:
        
        pattern = ""
        for num in nums:
            
            pattern += str(num)
            
        # patterns[pattern] += 1
        
        return pattern
    
    
    # O(m*(len(arr))^2) time,
    # O(S) space, S --> number of subarrays
    # Approach: string, array
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        
        for i in range(len(arr)):
            curr_pattern = None
            pattern_count = 0
            for j in range(i, len(arr), m):
                left, right = j, j + m
                if right > len(arr):
                    break
                    
                pattern = self.serializePattern(arr[left:right])
                
                if not curr_pattern:
                    curr_pattern = pattern
                
                if curr_pattern == pattern:
                    pattern_count += 1
                else:
                    curr_pattern = pattern
                    pattern_count = 1
                    
                if pattern_count == k:
                    return True
                
        
        return False