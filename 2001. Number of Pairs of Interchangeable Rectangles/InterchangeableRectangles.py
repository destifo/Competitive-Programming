from collections import defaultdict
import math
from typing import List


class Solution:
    
    
    # O(n) time,
    # O(n) space,
    # Approach: hashmap, math
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_rects = defaultdict(int)
        
        for width, height in rectangles:
            ratio = width/height
            ratio_rects[ratio] += 1
        
        pairs = 0
        for rects in ratio_rects.values():
            pairs += math.comb(rects, 2)
            
        return pairs