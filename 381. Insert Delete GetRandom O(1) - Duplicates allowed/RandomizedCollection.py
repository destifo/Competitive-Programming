import random


class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.indices = {}

        
    def insert(self, val: int) -> bool:
        found = val in self.indices
        val_indices = set()
        
        if found:
            val_indices = self.indices[val]
            
        n = len(self.nums)
        
        val_indices.add(n)
        self.indices[val] = val_indices
        self.nums.append(val)
        
        return not found
        

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        last_index = len(self.nums) - 1
        last_val = self.nums[last_index]
        if last_val == val:
            self.nums.pop()
            val_indices = self.indices[val]
            val_indices.remove(last_index)
            if len(val_indices) == 0:
                self.indices.pop(val)
            return True
            
        last_val_indices = self.indices[last_val]
        
        val_indices = self.indices[val]
        
        # print(val, val_indices)
        val_index = 0
        for val_index in val_indices:
            break
        
        # move the last val to a val index
        
        last_val_indices.add(val_index)
        last_val_indices.remove(last_index)
        self.nums[val_index] = last_val
        
        # remove val
        self.nums.pop()
        val_indices.remove(val_index)
        if len(val_indices) == 0:
            self.indices.pop(val)
            
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()