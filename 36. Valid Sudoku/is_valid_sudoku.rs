use std::collections::HashMap;

impl Solution {
    
    // O(1) time,
    // O(1) space,
    // Approach: hashtable, 
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let dimension = 9;
        let mut rows: Vec<HashMap<char, i32>> = vec![HashMap::new(); dimension];
        let mut cols: Vec<HashMap<char, i32>> = vec![HashMap::new(); dimension];
        
        let mut mini_squares: Vec<Vec<HashMap<char, i32>>> = vec![vec![HashMap::new();3];3];
        
        for row in 0..dimension {
            for col in 0..dimension {
                
                let val = board[row][col];
                let mut count = 0;
                if rows[row].contains_key(&val) {
                    count = *rows[row].get(&val).unwrap_or(&0);
                }
                rows[row].insert(val, count+1);
                
                count = 0;
                if cols[col].contains_key(&val) {
                    count = *cols[col].get(&val).unwrap_or(&0);
                }
                cols[col].insert(val, count+1);
                
                count = 0;
                if mini_squares[row/3][col/3].contains_key(&val) {
                    count = *mini_squares[row/3][col/3].get(&val).unwrap_or(&0);
                }
                mini_squares[row/3][col/3].insert(val, count+1);
                
            }
        }
        
        for row in 0..dimension {
            for col in 0..dimension {
                
                for (key, value) in &rows[row] {
                    if *value > 1 && *key != '.' {
                        return false;
                    }
                }
                
                for (key, value) in &cols[col] {
                    if *value > 1 && *key != '.' {
                        return false;
                    }
                }
                
                for (key, value) in &mini_squares[row/3][col/3] {
                    if *value > 1 && *key != '.' {
                        return false;
                    }
                }
                
            }
        }
        
        return true;
    }
}