from typing import List


class Solution:
    
    # O(n) time, 
    # O(1) space,
    # Apporach: math, 
    def average(self, salary: List[int]) -> float:
        return (sum(salary)-min(salary)-max(salary))/(len(salary)-2)