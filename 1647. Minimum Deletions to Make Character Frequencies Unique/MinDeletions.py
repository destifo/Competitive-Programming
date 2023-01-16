from collections import Counter


class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: counting, greedy, 
    def minDeletions(self, s: str) -> int:
        
        # we get the char freq
        char_count = Counter(s)
        
        # sort the freqs, in reverse order
        char_freq = [ cnt for cnt in char_count.values() ]
        char_freq.sort(reverse=True)
        
        # calculate the moves from available freqs
        min_moves = 0
        available_freqs = []
        for curr_freq in range(1, len(s)):
            # if our char freq array is depeleted, we exit
            if not char_freq:
                break
            
            # whenever we have available freq below or equal to curr_freq, we delete chars to make the freq equal to the one in the top of available_freqs stack
            available_freqs.append(curr_freq)
            while available_freqs and char_freq and char_freq[-1] == curr_freq:
                min_moves += (char_freq.pop()-available_freqs.pop())
                
            # for those counts we can't have available freqs to assign with, we just make their count to 0, and add their freq to our answer
            while char_freq and char_freq[-1] == curr_freq:
                min_moves += curr_freq
                char_freq.pop()
                
        return min_moves