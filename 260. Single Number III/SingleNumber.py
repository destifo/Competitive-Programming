from typing import List


class Solution:
    def rightShiftByK(self, k: int, num: int) -> int:
        
        return num >> k
    
    
    # O(n) time,
    # O(1) space,
    # Approach: bit manipulation
    def singleNumber1(self, nums: List[int]) -> List[int]:
        
        xor = 0
        
        for num in nums:
            xor ^= num
        
#         pos = 0
#         for i in range(32):
#             if (xor & 1<<i) > 0:
#                 pos = i
#                 break
                
#         mask_pos = a & (-a)
            
        k = 0
        while True:
            
            if (self.rightShiftByK(k, xor) & 1) == 1:
                break
                
            k += 1
            
        xor1, xor2 = 0, 0
        for num in nums:
            if (self.rightShiftByK(k, num) & 1) == 1:
                xor1 ^= num
            else:
                xor2 ^= num
                
        return [xor1, xor2]


    def singleNumber2(self, nums: List[int]) -> List[int]:
        
        xor = 0
        
        for num in nums:
            xor ^= num
        
#         pos = 0
#         for i in range(32):
#             if (xor & 1<<i) > 0:
#                 pos = i
#                 break
                
        mask_pos = xor & (-xor)
            
#         k = 0
#         while True:
            
#             if (self.rightShiftByK(k, xor) & 1) == 1:
#                 break
                
#             k += 1
            
        xor1, xor2 = 0, 0
        for num in nums:
            if mask_pos & num > 0:
                xor1 ^= num
            else:
                xor2 ^= num
                
        return [xor1, xor2]