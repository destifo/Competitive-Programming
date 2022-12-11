use std::cmp;

impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: monostack, 
    pub fn total_steps(nums: Vec<i32>) -> i32 {
        
        let mut stack = Vec::new();
        let mut dp = vec![0;nums.len()];
        
        for (i, num) in nums.iter().enumerate() {
            
            while !stack.is_empty() && nums[stack[stack.len()-1]] <= *num {
                let popped_steps = dp[stack.pop().unwrap()];
                dp[i] = cmp::max(dp[i], popped_steps);
            }
            
            if !stack.is_empty() {
                dp[i] += 1;
            }
            else {
                dp[i] = 0;
            }
            stack.push(i);
        }
        
        return *dp.iter().max().unwrap();
    }
}