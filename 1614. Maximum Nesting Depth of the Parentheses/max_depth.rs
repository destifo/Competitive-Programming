
use std::cmp::max;


impl Solution {
    
    // O(n) time,
    // O(1) space,
    // Approach: stack, counting
    pub fn max_depth(s: String) -> i32 {
        let mut pairs = 0;
        let mut ans = 0;
        
        for ch in s.chars() {
            match ch {
                '(' => pairs += 1,
                ')' => pairs -=1,
                _ => continue
            }
            ans = max(ans, pairs);
        }
        
        ans
    }
}