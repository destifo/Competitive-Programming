use std::collections::{BinaryHeap};


impl Solution {
    
    // O(n + klogn) time,
    // O(n) space,
    // Approach: heap, greedy, math
    pub fn min_stone_sum(piles: Vec<i32>, mut k: i32) -> i32 {
        let mut total = 0;
        let mut heap = BinaryHeap::new();
        
        for stones in &piles {
            total += *stones;
            heap.push(*stones);
        }
        
        while total > piles.len() as i32 && k > 0 {
            k -=1;
            let num = heap.pop().unwrap();
            let half = if num % 2 == 0 {num / 2} else {(num/2)+1};
            total -= (num-half);
            if half > 0 {
                heap.push(half);
            }
        }
        
        return total;
    }
}