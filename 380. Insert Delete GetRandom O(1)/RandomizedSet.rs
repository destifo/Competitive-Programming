use std::collections::HashMap;
use rand::Rng;

struct RandomizedSet {
    nums: Vec<i32>,
    num_index: HashMap<i32, usize>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */

// O(1) time,
// O(n) space,
// Approach: hashmap, 
impl RandomizedSet {

    fn new() -> Self {
        return RandomizedSet {
            nums: Vec::new(),
            num_index: HashMap::new(),   
        }
    }
    
    // O(1) time,
    fn insert(&mut self, val: i32) -> bool {
        
        if self.num_index.contains_key(&val) {
            return false;
        }
        
        self.nums.push(val);
        self.num_index.insert(val, self.nums.len()-1);
        return true;  
    }
    
    // O(1) time,
    fn remove(&mut self, val: i32) -> bool {
        if !self.num_index.contains_key(&val) {
            return false;
        }
        
        let n = self.nums.len();
        let last_val = self.nums[n-1];
        
        let val_index = *self.num_index.get(&val).unwrap_or(&0);
        self.num_index.insert(last_val, val_index);
        self.nums[val_index] = last_val;
        
        self.nums.pop();
        self.num_index.remove(&val);
        return true;
        
    }
    
    // O(1) time,
    fn get_random(&self) -> i32 {
        let index = rand::thread_rng().gen_range(0, self.nums.len());
        return self.nums[index];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */