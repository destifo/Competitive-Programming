# O(1) time, per call
# O(n) space,
# Approach: hashmap, hashset, design
from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.arr = {}
        self.freq = defaultdict(set)
        

    def add(self, number: int) -> None:
        if number in self.arr:
            self.freq[self.arr[number]].remove(number)
        
        self.arr[number] = self.arr.get(number, 0) + 1
        num_freq = self.arr[number]
        self.freq[num_freq].add(number)
        

    def deleteOne(self, number: int) -> None:
        if number not in self.arr:
            return
        
        self.freq[self.arr[number]].remove(number)
        self.arr[number] -= 1
        
        num_freq = self.arr[number]
        if num_freq == 0:
            self.arr.pop(number)
        else:
            self.freq[num_freq].add(number)
        

    def hasFrequency(self, frequency: int) -> bool:
        return len(self.freq[frequency]) > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)