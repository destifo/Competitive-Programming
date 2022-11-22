use std::cmp;
use std::collections::HashMap;

impl Solution {
    
    pub fn find_min_squares(remaining: i32, memo: &mut HashMap<i32, i32>) -> i32 {
        
        if memo.contains_key(&remaining) {
            return *memo.get(&remaining).unwrap_or(&0);
        }
        
        if remaining == 0 {
            return 0;
        }
        
        let mut min_squares = i32::MAX;
        for i in 1..remaining+1 {
            
            let square = (i*i);
            
            if square > remaining{
                break;
            }
            
            let answer = 1 + Solution::find_min_squares(remaining-square, memo);
            min_squares = cmp::min(min_squares, answer);
        }
        
        memo.insert(remaining, min_squares);
        return min_squares;
        
    }
    
    
    // O(n) time,
    // O(n) space,
    // Approach: dp with memoization,
    pub fn num_squares(n: i32) -> i32 {
        
        let mut memo = HashMap::new();
        return Solution::find_min_squares(n, &mut memo);
        
    }
}