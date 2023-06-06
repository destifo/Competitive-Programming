struct MyQueue {
    stack: Vec<i32>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {
    
    fn rellocate(stack: &mut Vec<i32>, temp: &mut Vec<i32>) {
        while stack.len() > 0 {
            temp.push(stack.pop().unwrap());
        }
    }

    fn new() -> Self {
        MyQueue { stack: Vec::new() }
    }
    
    fn push(&mut self, x: i32) {
        self.stack.push(x);
    }
    
    fn pop(&mut self) -> i32 {
        let mut temp = Vec::new();
        MyQueue::rellocate(&mut self.stack, &mut temp);
        let popped = temp.pop().unwrap();
        MyQueue::rellocate(&mut temp, &mut self.stack);
        return popped;
    }
    
    fn peek(&self) -> i32 {
        self.stack[0]
    }
    
    fn empty(&self) -> bool {
        self.stack.len() == 0
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