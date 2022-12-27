use std::collections::{BinaryHeap};


impl Solution {
    
    // O(nlogn) time,
    // O(n) space,
    // Approach: heap, 
    pub fn maximum_bags(capacity: Vec<i32>, rocks: Vec<i32>, mut additional_rocks: i32) -> i32 {
        let mut heap = BinaryHeap::new();
        for i in 0..rocks.len() {
            let curr_rock = rocks[i];
            let curr_capacity = capacity[i];
            
            heap.push(-(curr_capacity-curr_rock));
        }
        
        let mut max_fills = 0;
        while heap.len() > 0 {
            let num = -heap.pop().unwrap();
            if num > additional_rocks {
                return max_fills;
            }
            
            additional_rocks -= num;
            max_fills += 1;
        }
        
        return max_fills;
    }
}