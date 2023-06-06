impl Solution {
    
    // O(mn) time,
    // O(1) space,
    // Approach: matrix, 
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
        
        let mut set_first_row = false;
        let mut set_first_col = false;
        
        for row in 0..matrix.len() {
            for col in 0..matrix[0].len() {
                if matrix[row][col] == 0 {
                    if row == 0 {
                        set_first_row = true;
                    }
                    
                    if col == 0 {
                        set_first_col = true;
                    }
                    
                    matrix[row][0] = 0;
                    matrix[0][col] = 0;
                }
                
            }
        }
        
        // println!("{}", set_first_col);
        // making cells in a row zero
        for row in 1..matrix.len() {
            
            if matrix[row][0] != 0 {
                continue;
            }
            
            for col in 1..matrix[row].len() {
                matrix[row][col] = 0;
            }
            
        } 
        
        // making cells in a column zero
        for col in 1..matrix[0].len() {
            
            if matrix[0][col] != 0 {
                continue;
            }
            
            for row in 1..matrix.len() {
                matrix[row][col] = 0;
            }
            
        }
        
        if set_first_col {
            for row in 0..matrix.len() {
                matrix[row][0] = 0;
            }
        }        
        
        if set_first_row {
            for col in 0..matrix[0].len() {
                matrix[0][col] = 0;
            }
        }
        
    }
}