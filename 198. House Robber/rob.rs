use std::cmp;


impl Solution {
    
    // O(n^2) time,
    // O(n) space,
    // Approach: dp, bottom up, 
    pub fn rob(nums: Vec<i32>) -> i32 {
        
        let houses = nums.len();
        let mut dp = vec![0;houses];
        dp[houses-1] = nums[houses-1];
        
        for i in (0..houses-1).rev() {
            let mut next_max = 0;
            for j in (i+2..houses) {
                next_max = cmp::max(next_max, dp[j]);
            }
            
            dp[i] = cmp::max(nums[i]+next_max, dp[i+1]);
        }
        
        return dp[0];
    }


    // O(n) time,
    // O(n) space,
    // Approach: dp, bottom up, 
    pub fn rob2(nums: Vec<i32>) -> i32 {
        
        let houses = nums.len();
        let mut dp = vec![0;houses];
        dp[houses-1] = nums[houses-1];
        
        for i in (0..houses-1).rev() {
            let mut next_max = 0;
            if i+2 < houses {
                next_max = dp[i+2];
            }
            
            dp[i] = cmp::max(nums[i]+next_max, dp[i+1]);
        }
        
        return dp[0];
    }


    // O(n) time,
    // O(1) space,
    // Approach: dp, bottom up, 
    pub fn rob3(nums: Vec<i32>) -> i32 {
        
        let houses = nums.len();
        let mut curr_max = nums[houses-1];
        let mut next_max = 0;
        
        for i in (0..houses-1).rev() { 
            let temp = curr_max;
            curr_max = cmp::max(nums[i]+next_max, curr_max);
            next_max = temp;
        }
        
        return curr_max;
    }
}