from collections import deque


class MyStack:

    def __init__(self):
        self.nums = deque()
        

    def push(self, x: int) -> None:
        self.nums.append(x)
        

    def pop(self) -> int:
        temp = deque()
        last = None
        
        while self.nums:
            last = self.nums[0]
            temp.append(self.nums.popleft())
            
        while len(temp) > 1:
            self.nums.append(temp.popleft())
            
        return last
        

    def top(self) -> int:
        temp = deque()
        last = None
        
        while self.nums:
            last = self.nums[0]
            temp.append(self.nums.popleft())
            
        while len(temp):
            self.nums.append(temp.popleft())
            
        return last
        

    def empty(self) -> bool:
        return len(self.nums) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()