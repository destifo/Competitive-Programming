use std::collections::{VecDeque};


struct MyStack {
    queue: VecDeque<i32>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyStack {

    fn new() -> Self {
        MyStack { queue: VecDeque::new() }
    }
    
    fn push(&mut self, x: i32) {
        self.queue.push_back(x);
    }
    
    fn pop(&mut self) -> i32 {
        
        let mut temp = VecDeque::new();
        while self.queue.len() > 1 {
            let val = self.queue.pop_front().unwrap();
            temp.push_back(val);
        }
        
        let popped = self.queue.pop_front().unwrap();
        self.queue = temp;
        
        return popped;
    }
    
    fn top(&self) -> i32 {
        return self.queue[self.queue.len()-1];
    }
    
    fn empty(&self) -> bool {
        return self.queue.len() == 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * let obj = MyStack::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: bool = obj.empty();
 */