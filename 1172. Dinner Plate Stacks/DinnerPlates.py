import heapq


class DinnerPlates:
    
    '''
    
        design
        free slots: heap
        avoid repeated slots: hash set
        
        
        actions:
        push:
            - check leftmost free slot, add
            - if no free slot => create one and add to free slots
            - if curr slot reaches capacity, remove from the free slots and set
        
        pop:
            - remove element from right most
            - add that stack if not in free slots
            
            - if all stack is 
            
            
        popstack:
            - check if the index exists
            - remove if there's a val on top of the stack
            
        
    
    '''

    def __init__(self, capacity: int):
        self.k = capacity
        self.row = []
        self.free = []
        self.registered = set() # registered free slots
        
        

    def push(self, val: int) -> None:
        # add if no stack is available
        if not self.row:
            self.row.append([])
            heapq.heappush(self.free, 0)
            self.registered.add(0)
            
        # if no free slots, add extra stack
        if not self.free:
            self.row.append([])
            heapq.heappush(self.free, len(self.row)-1)
            self.registered.add(len(self.row)-1)
            
        # get left most stack with space and push
        # if the left most free index is larger than the row size, then reset the free slots and registered and add new stack
        index = self.free[0]
        if index >= len(self.row):
            self.free = [len(self.row)]
            self.registered = set([len(self.row)])
            self.row.append([])
            index = self.free[0]
        self.row[index].append(val)
        
        # check if no space at index
        if len(self.row[index]) == self.k:
            self.registered.remove(index)
            heapq.heappop(self.free)
            
        

    def pop(self) -> int:
        # get the last non empty stack
        index = len(self.row)-1
        while index >= 0 and not self.row[index]:
            self.row.pop()
            index -= 1
            
            
        if index == -1:
            return -1
        
        val = self.row[index].pop()
        if index not in self.registered:
            self.registered.add(index)
            heapq.heappush(self.free, index)
            
        return val
        

    def popAtStack(self, index: int) -> int:
        if len(self.row) < index or not self.row[index]:
            return -1
        
        val = self.row[index].pop()
        if index not in self.registered:
            self.registered.add(index)
            heapq.heappush(self.free, index)
            
        return val
        


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)