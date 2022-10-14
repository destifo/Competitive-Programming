from collections import deque
import functools
from typing import List


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: sorting,
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = deque()
        letter_logs = []
        
        for log in logs:
            log_info = log.split()
            data_piece = log_info[1]
            
            if data_piece.isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
                
        def compareLogs(log1, log2) -> int:
            log1_info = log1.split()
            log2_info = log2.split()
            identifier1 = log1_info[0]
            identifier2 = log2_info[0]
            content1 = log1[len(identifier1)+1:]
            content2 = log2[len(identifier2)+1:]
            
            if content1 > content2: return 1
            elif content2 > content1:   return -1
            else:
                if identifier1 > identifier2:   return 1
                else:   return -1
            
        ordered_logs = sorted(letter_logs, key=functools.cmp_to_key(compareLogs))
        while digit_logs:
            ordered_logs.append(digit_logs.popleft())
        
        return ordered_logs