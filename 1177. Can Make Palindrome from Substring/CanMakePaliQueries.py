from collections import defaultdict
from typing import List


class Solution:
    
    def getWindowCount(self, start, end, char_map):
        
        at_start = char_map[start]
        at_end = char_map[end+1]
        window_count = {}
        
        for ch, cnt in at_end.items():
            window_count[ch] = cnt-at_start[ch]
            
        return window_count
    
    
    def isPossible(self, char_map, start, end, k) -> bool:
        
        window_count = self.getWindowCount(start, end, char_map)
        odd_count = 0

        for cnt in window_count.values():
            if cnt % 2 == 1:
                odd_count += 1
                
        return odd_count//2 <= k
    
    
    # O(len(s) + len(queries)) time, getting the chars in current window is O(1) cause we iterate over only 26 times, 
    # O(len(s)) space,
    # Approach: prefix sum, hashmap, 
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        
        char_count = defaultdict(int)
        count_at_index = [defaultdict(int)]
        
        for ch in s:
            char_count[ch] += 1
            count_at_index.append(char_count.copy())

        answer = [False for _ in range(len(queries))]
        for index, query in enumerate(queries):
            start, end, k = query
            if self.isPossible(count_at_index, start, end, k):
                answer[index] = True
        
        return answer