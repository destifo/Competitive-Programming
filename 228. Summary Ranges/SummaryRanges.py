from typing import List


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: stack, string, 
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        
        curr_range = []
        for num in nums:
            if curr_range and abs(num-int(curr_range[-1])) <= 1:
                if len(curr_range) > 1:
                    curr_range.pop()
            elif curr_range:
                rannge = "->".join(curr_range)
                if rannge:  answer.append(rannge)
                curr_range = []
            curr_range.append(str(num))
        
        rannge = "->".join(curr_range)
        if rannge:  answer.append(rannge)
        
        return answer