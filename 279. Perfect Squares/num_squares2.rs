use std::cmp::min;

impl Solution {
    
    // O(nsqrt(n)) time,
    // O(n) space,
    // Approach: bottom up dp, 
    pub fn num_squares(n: i32) -> i32 {
        let mut dp = vec![n;n as usize+1];
        dp[0] = 0;
        
        for i in 1..=n as usize {
            for j in 1..=i {
                let sq_num = j*j;
                if sq_num > i {
                    break;
                }
                dp[i] = min(dp[i], 1 + dp[(i-sq_num)]);
            }
        }
        
        dp[n as usize]
    }
}