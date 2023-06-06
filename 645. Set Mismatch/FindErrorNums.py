from typing import Counter, List


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: hashmap, 
    def findErrorNums1(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        
        deleted = None
        duplicate = None
        
        for num in range(1, len(nums)+1):
            if num not in nums_count:
                deleted = num
            elif nums_count[num] == 2:
                duplicate = num
        
        return [duplicate, deleted]


    # O(n) time,
    # O(1) space,
    # Approach: array, 
    def findErrorNums2(self, nums: List[int]) -> List[int]:
        
        deleted = None
        duplicate = None
        
        for num in nums:
            nums[(num-1)%10000] += 10000
        
        for index, num in enumerate(nums):
            if num > 20000:
                duplicate = index + 1
            elif num < 10001:
                deleted = index + 1
        
        # print(nums)
        return [duplicate, deleted]

    
    def rightShiftByK(self, num: int, k: int) -> int:
        
        return num >> k
    
    
    def findDuplicateAndMissing(self, nums: List[int], num1: int, num2: int) -> int:
        
        for num in nums:
            
            if num == num1:
                return num1, num2
            elif num == num2:
                return num2, num1
    
    
    # O(n) time,
    # O(1) space,
    # Approach: bit manipulation, 
    def findErrorNums3(self, nums: List[int]) -> List[int]:
        
        xor = 0
        
        for i in range(1, len(nums)+1):
            num = nums[i-1]
            
            xor ^= num
            xor ^= i
        
        k = 0
        while True:
            
            if (self.rightShiftByK(xor, k) & 1) == 1:
                break
                
            k += 1
            
        xor1, xor2 = 0, 0
        
        for i in range(1, len(nums)+1):
            num = nums[i-1]
            
            if (self.rightShiftByK(i, k) & 1) == 1:
                xor1 ^= i
            else:
                xor2 ^= i
                
            if (self.rightShiftByK(num, k) & 1) == 1:
                xor1 ^= num
            else:
                xor2 ^= num
                
        
        duplicate, missing = self.findDuplicateAndMissing(nums, xor1, xor2)
        
        return [duplicate, missing]