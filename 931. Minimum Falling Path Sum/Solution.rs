use std::cmp;

impl Solution {
    pub fn min_falling_path_sum(matrix: Vec<Vec<i32>>) -> i32 {
        let mut matrix = matrix;
        let ROWS = matrix.len() as i32;
        let COLS = matrix[0].len() as i32;
        
        for row in (0..ROWS-1).rev() {
            for col in 0..COLS {
                let directions = vec![(1, 0), (1, -1), (1, 1)];
                let mut min_next = i32::MAX;
                for (x, y) in directions {
                    let new_row = row+x;
                    let new_col = col+y;
                    if 0 <= new_row && new_row < ROWS && 0 <= new_col && new_col < COLS {
                        min_next = cmp::min(min_next, matrix[new_row as usize][new_col as usize])
                    }
                }
                matrix[row as usize][col as usize] += min_next;
            }
        }
        
        return *matrix[0].iter().min().unwrap();
    }
}