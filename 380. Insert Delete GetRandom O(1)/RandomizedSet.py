import random


class RandomizedSet:

    def __init__(self):
        self.data = []
        self.indices = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.indices:
            self.indices[val] = len(self.data)
            self.data.append(val)
            return True
        
        return False
        

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        val_index, last_index = self.indices[val], self.indices[self.data[-1]]
        self.data[val_index], self.data[last_index] = self.data[last_index], self.data[val_index]
        self.data.pop()
        self.indices.pop(val)
        if val_index < len(self.data):
            self.indices[self.data[val_index]] = val_index
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()