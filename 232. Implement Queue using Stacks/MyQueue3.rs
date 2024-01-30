struct MyQueue {
    data: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {

    fn new() -> Self {
        Self {
            data: vec![]
        }
    }
    
    fn push(&mut self, x: i32) {
        self.data.push(x);
    }
    
    fn pop(&mut self) -> i32 {
        let mut reversed: Vec<i32> = vec![];
        while let Some(value) = self.data.pop() {
            reversed.push(value);
        }
        let ans = reversed.pop().unwrap();
        
        while let Some(value) = reversed.pop() {
            self.data.push(value);
        }
        
        ans
    }
    
    fn peek(&self) -> i32 {
        self.data[0]
    }
    
    fn empty(&self) -> bool {
        self.data.len() == 0
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