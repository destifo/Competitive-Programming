'''
https://leetcode.com/problems/online-election/
'''


from typing import List


class TopVotedCandidate:

    # O(n) time, to build the vote result at every index,
    # O(n) space, 
    # Approach: HashTable
    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.vote_result = {}
        
        maxVote = 1
        frqntVote = persons[0]
        vote_count = {}
        for i in range(len(persons)):
            person = persons[i]
            vote_count[person] = vote_count.get(person, 0) + 1
            if vote_count[person] >= maxVote:
                frqntVote = person
                maxVote = vote_count[person]
                
            self.vote_result[i+1] = frqntVote
                

    # O(logn) time,
    # O(1) space, 
    # Approach: binary search,
    def q(self, t: int) -> int:
        times = self.times
        vote_result = self.vote_result
        
        def binarySearch(start, end):
            mid = (start + end) // 2
            if times[mid] == t or (times[mid] < t and times[mid+1] > t):
                return mid
            elif start == end - 1 and times[end] <= t:
                return end
            elif times[mid] > t:
                return binarySearch(start, mid)
            else:
                return binarySearch(mid, end)
          
        timeIndex = binarySearch(0, len(times)-1) + 1
        return vote_result[timeIndex]
            

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)