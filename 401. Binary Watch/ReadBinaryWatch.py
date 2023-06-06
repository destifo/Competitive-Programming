from typing import List, Set


class Solution:
    
    def getEstimation(self, tokens: int, bits: List[int], used: Set[int], tot: int, answer: List[int]) -> None:
        
        if tokens == 0:
            if tot < 60:
                answer.append(str(tot))
            return
        
        for bit in bits:
            if bit in used: continue
                
            used.add(bit)
            self.getEstimation(tokens-1, bits, used, tot+bit, answer)
            used.remove(bit)
            
    
    # O(turnedOn * 2^turnedOn) time,
    # O(turnedOn * 2^tunrnedOn) space,
    # Approach: backtracking, 
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        possible_times = set()
        
        for i in range(turnedOn+1):
            hours = []
            minutes = []
            if i != 0:
                self.getEstimation(min(i, 4), [1, 2, 4, 8], set(), 0, hours)
            else:
                hours.append('0')
                
            if turnedOn-i != 0:
                self.getEstimation(min(turnedOn-i, 6), [1, 2, 4, 8, 16, 32], set(), 0, minutes)
            else:
                minutes.append('00')
                
            for hour in hours:
                for minute in minutes:
                    
                    if int(hour) > 11:
                        continue
                    
                    if len(minute) == 1:
                        minute = '0'+ minute
                        
                    time = hour + ':' + minute
                    
                    possible_times.add(time)
                    
        return list(possible_times)