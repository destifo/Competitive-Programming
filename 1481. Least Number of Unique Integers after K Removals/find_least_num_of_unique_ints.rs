use std::collections::{BinaryHeap, HashMap};
use std::cmp::{Reverse, min};


impl Solution {
    
    // O(klogn + n) time,
    // O(n) space,
    // Approach: heap, hash map
    pub fn find_least_num_of_unique_ints(arr: Vec<i32>, mut k: i32) -> i32 {
        let mut heap: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();
        let mut count: HashMap<i32, i32> = HashMap::new();
        for num in arr {
            *count.entry(num).or_insert(0) += 1;
        }
        
        for (num, cnt) in count {
            heap.push(Reverse((cnt, num)));
        }

        while k > 0 && !heap.is_empty() {
            if let Some(Reverse((num_count, _))) = heap.pop() {
                if k < num_count {
                    heap.push(Reverse((0, 0)))
                } 
                k -= min(k, num_count);
            }
        }
        
        heap.len() as i32
    }
}