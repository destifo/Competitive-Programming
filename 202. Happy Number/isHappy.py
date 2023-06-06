'''
https://leetcode.com/problems/happy-number/
'''


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: hashmap
    def isHappy(self, n: int) -> bool:
        vstd = set()
        
        def isHappy(num:int) -> bool:
            if num == 1:    return True
            
            if num in vstd:    return False
            
            vstd.add(num)
            num = str(num)
            tot = 0
            
            for digit in num:
                tot +=(int(digit) ** 2)
                
            return isHappy(tot)
        
        return isHappy(n)