impl Solution {
    
    // O(n) time,
    // O(n) space,
    // Approach: dynamic programming, array
    pub fn climb_stairs(n: i32) -> i32 {
        if n < 2 {
            return 1;
        }
        
        let n = n as usize;
        let mut dp = vec![0;n];
        dp[n-1] = 1;
        dp[n-2] = 2;
        
        for i in (0..n-2).rev() {
            dp[i] = dp[i+1] + dp[i+2];
        }
        
        return dp[0];
    }


    // O(n) time,
    // O(1) space,
    // Approach: dynamic programming, bottom up, 
    pub fn climb_stairs2(n: i32) -> i32 {
        
        if n < 2 {
            return n;
        }
        
        let mut curr = 2;
        let mut prev = 1;
        
        for i in 0..n-2 {
            
            let temp = curr;
            curr += prev;
            prev = temp;   
        }
        
        return curr;
    }
}