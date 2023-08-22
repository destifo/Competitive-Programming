class Solution:
    
    def getChar(self, num: int) -> str:
        if num == 0:
            return "Z"
        char_offset = 64
        return chr(num+char_offset)
    
    
    def getTitle(self, columnNumber: int) -> str:
        if columnNumber <= 26:
            return self.getChar(columnNumber)
        
        return self.getTitle(columnNumber//26 + (-1 if columnNumber%26 == 0 else 0)) + self.getChar(columnNumber%26)
    
    
    # O(logn) time,
    # O(logn) space,
    # Approach: recursion, 
    def convertToTitle(self, columnNumber: int) -> str:
        return self.getTitle(columnNumber)