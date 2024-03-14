use std::collections::HashMap;


impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: prefix sum, hash map
    pub fn num_subarrays_with_sum(nums: Vec<i32>, goal: i32) -> i32 {
        let mut prefix_map = HashMap::new();
        let mut agg = 0;
        let mut ans = 0;
        
        prefix_map.insert(0, 1);
        
        for num in nums {
            agg += num;
            let target = agg-goal;
            if let Some(count) = prefix_map.get(&target) {
                ans += *count;
            }
            *prefix_map.entry(agg).or_insert(0) += 1;
        }
        
        ans
    }
}