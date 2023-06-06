use std::cmp;


impl Solution {
    
    // O(n) time,
    // O(1) space,
    // Approach: greedy, 
    pub fn maximum_top(nums: Vec<i32>, k: i32) -> i32 {
        if k % 2 == 1 && nums.len() == 1 {
            return -1;
        }
        
        let range = cmp::min(nums.len(), k as usize);
        let mut max_val = 0;
        for i in 0..range {
            if i == range-1 && (k as usize) <= nums.len() {
                continue;
            }
            max_val = cmp::max(max_val, nums[i]);
        }
        
        if (k as usize) < nums.len() {
            max_val = cmp::max(max_val, nums[k as usize]);
        }
        
        return max_val
    }
}