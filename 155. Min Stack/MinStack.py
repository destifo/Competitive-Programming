#well, I had help on this one to be honest
class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int):
        self.stack.append(val)
        if (len(self.min_stack) == 0):
            self.min_stack.append(val)
            return
        self.min_stack.append(min(val, self.min_stack[-1]))

        
    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.min_stack[-1]
        


#Your MinStack object will be instantiated and called as such:
obj = MinStack()
#obj.push(-2)
#obj.push(0)
obj.push(-3)
print(obj.getMin())
#print(obj.pop())
#print(obj.top())
#print(obj.getMin())