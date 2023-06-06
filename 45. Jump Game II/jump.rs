use std::cmp;


impl Solution {

    // O(n*max(nums[i])) time,
    // O(n) space,
    // Approach: dp, bottom up, 
    pub fn jump(nums: Vec<i32>) -> i32 {
        if nums.len() < 2 {
            return 0;
        }
        
        let mut dp = vec![i32::MAX-2;nums.len()];
        dp[nums.len()-1] = 0;
        dp[nums.len()-2] = 1;
        
        
        for i in (0..nums.len()-1).rev() {
            let jump = nums[i] as usize;
            for j in 1..jump+1 {
                if i+j >= nums.len() {
                    break;
                }
                dp[i] = cmp::min(dp[i], 1+dp[i+j]);
            }
        }
        
        return dp[0];
    }


    // O(n) time,
    // O(1) space,
    // Approach: greedy, 
    pub fn jump(nums: Vec<i32>) -> i32 {
        let mut jumps = 0;
        let mut next_max = 0;
        let mut curr_max = 0;
        
        for i in 0..nums.len() {
            next_max = cmp::max(next_max, i as i32 +nums[i]);
            
            if curr_max >= nums.len()-1 {
                return jumps;
            }
            
            if i == curr_max {
                jumps += 1;
                curr_max = next_max as usize;
            }
        }
        
        return -1;
    }
}