use std::collections::HashMap;
use std::cmp::max;


impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: sliding window, hash map, 
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut count = HashMap::new();
        let (mut left, mut right) = (0, 0);
        let mut max_freq = 0;
        let mut ans = 0;
        
        while right < n {
            *count.entry(nums[right]).or_default() += 1;
            max_freq = max(max_freq, *count.get(&nums[right]).unwrap());
            while max_freq > k {
                let num_freq = *count.get(&nums[left]).unwrap();
                count.insert(nums[left], num_freq-1);
                if num_freq == max_freq {
                    max_freq -= 1;
                }
                left += 1;
            }
            right += 1;
            ans = max(ans, (right-left) as i32);
        }
        
        ans
    }
}