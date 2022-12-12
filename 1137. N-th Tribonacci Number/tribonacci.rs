impl Solution {
    
    // O(n) time,
    // O(1) space,
    // Approach: dp, bottom up
    pub fn tribonacci(n: i32) -> i32 {
        
        let mut dp = vec![1, 1, 0];
        if n < 3 {
            return dp[2-n as usize];
        }
        
        for i in 0..n-2 {
            let sum = dp[0] + dp[1] + dp[2];
            dp[2] = dp[1];
            dp[1] = dp[0];
            dp[0] = sum;
        }
        
        return dp[0];     
    }
}