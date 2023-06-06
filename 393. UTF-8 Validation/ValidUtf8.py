'''
https://leetcode.com/problems/utf-8-validation/
'''


from typing import List


class Solution:
    # O(n) time,
    # O(1) space,
    # Approach: array,
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)
        
        def findNumBytes(num: int) -> int:
            if num < 128:
                return 1
            
            if num >= 192 and num < 224:
                return 2
            
            if num >= 224 and num < 240:
                return 3
            
            if num >= 240 and num < 248:
                return 4
            
            return -1
        
        i = 0
        while i < n:
            num = data[i]
            byte_num = findNumBytes(num)
            # print(byte_num)
            if byte_num == -1:  return False
            
            subseq_num_range = 128, 192
            
            data_left = n - i
            if data_left < byte_num - 1:    return False
            
            j = i+1
            while j < byte_num + i:
                num = data[j]
                if num < subseq_num_range[0] or num >= subseq_num_range[1]: return False
                j +=1
                
            i = j
            
        return True   