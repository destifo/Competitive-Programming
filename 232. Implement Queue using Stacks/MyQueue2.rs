struct MyQueue {
    stack1: Vec<i32>,
    stack2: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */

// O(1) amortized time,
// O(n) space,
// Approach: stack, design
impl MyQueue {

    fn new() -> Self {
        MyQueue { stack1: Vec::new(), stack2: Vec::new() }
    }
    
    fn push(&mut self, x: i32) {
        self.stack1.push(x);
    }
    
    fn pop(&mut self) -> i32 {
        
        if self.stack2.len() < 1 {
            while self.stack1.len() > 0 {
                self.stack2.push(self.stack1.pop().unwrap());
            }
        }
        
        self.stack2.pop().unwrap()
    }
    
    fn peek(&self) -> i32 {
        if self.stack2.len() > 0{
            return self.stack2[self.stack2.len()-1];
        }
        
        self.stack1[0]
    }
    
    fn empty(&self) -> bool {
        self.stack1.len() == 0 && self.stack2.len() == 0
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.empty();
 */