impl Solution {
    
    // O(n*logk) time,
    // O(n) space,
    // Approach: bottom up dp, 
    pub fn number_of_arrays(s: String, k: i32) -> i32 {
        let MOD = (10 as i32).pow(9) + 7;
        let mut dp = vec![0;s.len() + 1];
        dp[s.len()] = 1;
        
        for (start, c) in s.char_indices().rev() {
            if c == '0' {
                continue;
            }
            for end in start+1..s.len()+1 {
                let curr_num = s[start..end].parse::<i64>().unwrap();
                if curr_num > k as i64 {
                    break;
                }
                dp[start] += dp[end];
                dp[start] %= MOD;
            }
        }
        
        return dp[0];
    }
}