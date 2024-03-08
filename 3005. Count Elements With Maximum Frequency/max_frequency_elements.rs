use std::collections::HashMap;


impl Solution {
    
    // O(n) time, two passes
    // O(n) space,
    // Approach: hashmap, counting
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut count = HashMap::new();
        
        let mut max_freq = 0;
        for num in nums {
            *count.entry(num).or_insert(0) += 1;
            if let Some(curr_count) = count.get(&num) {
                if *curr_count > max_freq {
                    max_freq = *curr_count;
                }
            }
        }
        
        let mut max_freq_count = 0;
        for value in count.values() {
            if *value == max_freq {
                max_freq_count += 1;
            }
        }
        
        max_freq * max_freq_count
    }
}