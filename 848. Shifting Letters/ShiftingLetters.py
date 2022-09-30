from typing import List


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: reverse thinking, 
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        tot_shifts = 0
        n = len(shifts)
        str_lst = list(s)
        
        def shift(tot_shifts, index) -> None:
            asci = ord(s[index]) - 97
            asci += tot_shifts
            asci %= 26
            asci += 97
            after_shift = chr(asci)
            str_lst[index] = after_shift
        
        for i in range(n-1, -1, -1):
            tot_shifts += shifts[i]
            shift(tot_shifts, i)
            
        return ''.join(str_lst)