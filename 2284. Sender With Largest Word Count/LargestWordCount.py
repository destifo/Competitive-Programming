from collections import defaultdict
from typing import List


class Solution:
    
    def countWords(self, message):
        spaces = 0
        for ch in message:
            if ch == " ":
                spaces += 1
                
        return spaces+1
    
    
    # O(len(senders)*len(message)) time,
    # O(len(senders)) space,
    # Approach: counting, hashmap
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        '''
        goal: to find the person who have sent many words
        
        approach: count the words in a message and add it to the word count of respective sender, then return the sender with the max word count
        '''
        
        # init a word count defaultdict for number of words sent by a sender
        word_count = defaultdict(int)
        
        # do a word count on a message, add that count to the sender total count
        for i in range(len(messages)):
            sender = senders[i]
            message = messages[i]
            word_count[sender] += self.countWords(message)
            
        # return sender with max_count
        count_to_sender = [ (cnt, sender) for sender, cnt in word_count.items() ]
        count_to_sender.sort()
        
        return count_to_sender[-1][1]