import math
from typing import List


class Solution:
    
    def findOrdering(self, index, books, curr_width, max_height, width_limit, memo):
        
        if index >= len(books):
            return max_height
        
        if (index, curr_width) in memo:
            return memo[(index, curr_width)]
        
        same_row = math.inf
        skip_row = math.inf
        book = books[index]
        
        if curr_width + book[0] <= width_limit:
            same_row = self.findOrdering(index+1, books, curr_width + book[0], max(max_height, book[1]), width_limit, memo)
        
        if index != 0:
            skip_row = max_height + self.findOrdering(index+1, books, book[0], book[1], width_limit, memo)
        
        memo[(index, curr_width)] = min(same_row, skip_row)
        return memo[(index, curr_width)]
        
    
    # O(n) time,
    # O(n*shelfWidth) space,
    # Approach: dp with memoization, 
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        return self.findOrdering(0, books, 0, 0, shelfWidth, {})
        