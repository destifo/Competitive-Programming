impl Solution {
    
    // O(sqrt(c)) time,
    // O(1) space,
    // Approach: two pointers, math
    pub fn judge_square_sum(c: i32) -> bool {
        
        let mut left = 0;
        let mut right = (c as f64).sqrt() as i64 + 1;
                
        while left <= right {
            
            let square_sum = (left*left) as i64 + (right*right) as i64;
            
            if square_sum == c as i64 {
                return true;
            }
            else if square_sum < c as i64 {
                left += 1;
            }
            else {
                right -= 1;
            }
            
        }
        
        return false;
        
    }
}