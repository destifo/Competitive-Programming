class Solution:
    
    # O(n) time,
    # O(1) space,
    # Approach: counting, 
    def minOperations(self, s: str) -> int:
        
        '''
        
        ops1 => 0 in odd position, 1 in even
        ops2 => 0 in even, 1 in odd
        
        '''
        
        ops1, ops2 = 0, 0
        
        for i, ch in enumerate(s):
            
            if i % 2 == 0:
                if ch == '0':
                    ops1 += 1
                else:
                    ops2 += 1
            else:
                if ch == '1':
                    ops1 += 1
                else:
                    ops2 += 1
                    
        return min(ops1, ops2)