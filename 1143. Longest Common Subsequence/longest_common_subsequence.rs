use std::cmp;


impl Solution {
    
    
    // O(n*m) time,
    // O(n*m) space,
    // Approach: dp, bottom up, tablulation
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        
        let mut dp = vec![vec![0;text2.len()+1];text1.len()+1];
        let text1: Vec<char> = text1.chars().collect();
        let text2: Vec<char> = text2.chars().collect();
        let mut lcs = 0;
        
        for i in (0..text1.len()).rev() {
            for j in (0..text2.len()).rev() {
                
                if text1[i] == text2[j] {
                    // println!("hey");
                    dp[i][j] = dp[i+1][j+1] + 1;
                }
                else {
                    dp[i][j] = cmp::max(dp[i+1][j], dp[i][j+1]);
                }
                
                lcs = cmp::max(lcs, dp[i][j]);
            }
        }
        
        return lcs;
    }
}