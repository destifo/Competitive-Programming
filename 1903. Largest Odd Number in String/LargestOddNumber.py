class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: string, 
    def largestOddNumber(self, num: str) -> str:
        index = 0
        
        for i, digit in enumerate(num):
            digit = int(digit)
            if digit % 2 == 1:
                index = i+1
                
        return num[:index]
    
    
    # O(n) time,
    # O(1) space,
    # Approach: string, 
    def largestOddNumber2(self, num: str) -> str:        
        
        '''
            smart solution
        '''
        
        for i in range(len(num)-1, -1, -1):
            digit = int(num[i])
            if digit % 2 == 1:
                return num[:i+1]
                
        return ""