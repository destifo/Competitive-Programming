use std::cmp;


impl Solution {
    
    // O(n^2) time,
    // O(1) space,
    // Approach: dp, bottom up, 
    pub fn min_falling_path_sum(matrix: Vec<Vec<i32>>) -> i32 {
        let ROWS = matrix.len();
        let COLS = matrix[0].len();
        let mut matrix = matrix;
        
        for row in (0..ROWS-1).rev() {
            for col in 0..COLS {
                
                let bottom_left = if (col != 0) { matrix[row+1][col-1] } else {i32::MAX};
                let bottom_middle = matrix[row+1][col];
                let bottom_right = if (col < COLS-1) {matrix[row+1][col+1]} else {i32::MAX};
                
                matrix[row][col] += cmp::min(bottom_left, cmp::min(bottom_middle, bottom_right));
                
            }
        }
        
        return *matrix[0].iter().min().unwrap();
    }
}