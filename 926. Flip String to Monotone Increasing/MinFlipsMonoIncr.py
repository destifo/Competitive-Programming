class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: prefix sum
    def minFlipsMonoIncr(self, s: str) -> int:
        '''
        monotone increasing is, taking index i, all vals before index i are 0, and all vals starting from index i are 1. 
        
        count no of 0's and 1's at each index, 
        
        calculate flips at index i, by adding number of 1's before index i (cause we need to change those into 0's) with number of 0's starting from index i(change those into 1's)
        
        then return min flip from the flips at each index
        '''
        
        # create flips array for flips needed to make string monotone at an index
        flips = [0 for _ in range(len(s)+1)]
        
        # do forward pass and count 1's to change to 0 at each index, and add to flips[i]
        ones = 0
        for i in range(len(s)):
            flips[i] += ones
            if s[i] == '1':
                ones += 1
                
        # considering to change all string to 0's
        flips[len(s)] = ones
        # do backward pass to get flips needed at each index to convert 0's to 1's
        zeroes = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                zeroes += 1
            flips[i] += zeroes
        
        # return min flip
        return min(flips)