impl Solution {
    
    fn get_sum(row: i32, col: i32, mat: &Vec<Vec<i32>>) -> i32 {
        let mut left_sum = 0;
        let mut top_sum = 0;
        
        if col-1 >= 0 {
            left_sum = mat[row as usize][(col-1) as usize];
        }
        
        if row-1 >= 0 {
            top_sum = mat[(row-1) as usize][col as usize];
        }
        
        return left_sum + top_sum;
    }
    
    
    // O(n*m) time,
    // O(n*m) space,
    // Approach: prefix sum, 
    pub fn matrix_block_sum(mat: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let ROWS = mat.len();
        let COLS = mat[0].len();
        let mut prefix_sum = vec![vec![0;COLS];ROWS];
        
        for i in 0..ROWS {
            for j in 0..COLS {
                prefix_sum[i][j] = mat[i][j] + Solution::get_sum(i as i32, j as i32, &prefix_sum);
                if i > 0 && j > 0 {
                    prefix_sum[i][j] -= prefix_sum[i-1][j-1];
                }
            }
        }

        let mut ans = vec![vec![0;COLS];ROWS];
        for i in 0..ROWS {
            for j in 0..COLS {
                let start_row = if (i as i32 - k) >= 0 {i-k as usize} else {0};
                let start_col = if (j as i32 - k) >= 0 {j-k as usize} else {0};
                let end_row = if (i as i32 + k) < ROWS as i32 {i+k as usize} else {ROWS-1};
                let end_col = if (j as i32 + k) < COLS as i32 {j+k as usize} else {COLS-1};
                
                ans[i][j] = prefix_sum[end_row][end_col];
                if start_row > 0 && start_col > 0 {
                    ans[i][j] += prefix_sum[start_row-1][start_col-1];
                }
                if start_row > 0 {
                    ans[i][j] -= prefix_sum[start_row-1][end_col]
                }
                if start_col > 0 {
                    ans[i][j] -= prefix_sum[end_row][start_col-1];
                }
                
            }
        }

        return ans;
    }
}